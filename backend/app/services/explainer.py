"""Rule-based root cause analysis (FR-17, Table 2)."""

SENSOR_NAMES = {
    "temp_c": "temperature",
    "pressure_bar": "pressure",
    "neutron_flux": "neutron flux",
    "vibration_ms2": "vibration",
}

CAUSE_RULES = [
    {
        "pattern": {"temp_c": "high", "pressure_bar": "low"},
        "cause_fa": "The abnormal temperature rise is probably caused by a cooling pump failure",
        "cause_en": "Abnormal temperature rise likely caused by coolant pump failure",
    },
    {
        "pattern": {"neutron_flux": "low", "temp_c": "low"},
        "cause_fa": "The drop in neutron flux and temperature is probably caused by control rod insertion",
        "cause_en": "Neutron flux and temperature drop likely caused by control rod insertion",
    },
    {
        "pattern": {"vibration_ms2": "high"},
        "cause_fa": "The increase in vibration is probably caused by a mechanical imbalance",
        "cause_en": "Increased vibration likely caused by mechanical imbalance",
    },
    {
        "pattern": {"pressure_bar": "high", "temp_c": "high"},
        "cause_fa": "The increase in pressure and temperature is probably caused by a cooling circuit blockage",
        "cause_en": "Pressure and temperature rise likely caused by coolant circuit blockage",
    },
]


def classify_sensor_level(value: float, baseline: float, threshold_pct: float = 0.05) -> str:
    if value > baseline * (1 + threshold_pct):
        return "high"
    if value < baseline * (1 - threshold_pct):
        return "low"
    return "normal"


def infer_probable_cause(
    sensor_values: dict[str, float],
    baselines: dict[str, float] | None = None,
    lang: str = "fa",
) -> tuple[str, list[str]]:
    """Return probable cause and list of affected sensors."""
    baselines = baselines or {
        "temp_c": 300.0,
        "pressure_bar": 150.0,
        "neutron_flux": 1000.0,
        "vibration_ms2": 0.5,
    }

    levels = {
        col: classify_sensor_level(sensor_values.get(col, baselines[col]), baselines[col])
        for col in baselines
    }

    affected = [SENSOR_NAMES[col] for col, level in levels.items() if level != "normal"]

    for rule in CAUSE_RULES:
        if all(levels.get(k) == v for k, v in rule["pattern"].items()):
            cause_key = "cause_fa" if lang == "fa" else "cause_en"
            return rule[cause_key], affected

    cause_key = "cause_fa" if lang == "fa" else "cause_en"
    default_fa = "An anomaly pattern was identified; the exact cause needs further investigation"
    default_en = "Anomaly pattern detected; root cause requires further investigation"
    return (default_fa if lang == "fa" else default_en), affected

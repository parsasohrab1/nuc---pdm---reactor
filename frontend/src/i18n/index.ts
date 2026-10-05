export type Lang = "fa" | "en";

const translations = {
  fa: {
    title: "PdM-Nuclear Dashboard",
    statusNormal: "Status: Normal",
    statusAlert: "Anomaly alert!",
    temperature: "Temperature (°C)",
    pressure: "Pressure (bar)",
    neutronFlux: "Neutron flux",
    vibration: "Vibration (m/s²)",
    alertsHistory: "Alerts history",
    time: "Time",
    confidence: "Confidence",
    cause: "Probable cause",
    sensors: "Sensors",
    noAlerts: "No alerts have been recorded yet",
    langToggle: "English",
    backendOnline: "API connected",
    backendOffline: "API disconnected",
    alertPopup: "Anomaly detected!",
  },
  en: {
    title: "PdM-Nuclear Dashboard",
    statusNormal: "Status: Normal",
    statusAlert: "Anomaly Alert!",
    temperature: "Temperature (°C)",
    pressure: "Pressure (bar)",
    neutronFlux: "Neutron Flux",
    vibration: "Vibration (m/s²)",
    alertsHistory: "Alert History",
    time: "Time",
    confidence: "Confidence",
    cause: "Probable Cause",
    sensors: "Sensors",
    noAlerts: "No alerts recorded yet",
    langToggle: "فارسی",
    backendOnline: "API Connected",
    backendOffline: "API Offline",
    alertPopup: "Anomaly Detected!",
  },
} as const;

export function t(lang: Lang, key: keyof (typeof translations)["fa"]): string {
  return translations[lang][key];
}

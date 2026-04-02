# Product Guidelines: LeafCloudIoT

## Prose Style
- **Technical Clarity:** Documentation and code comments should be concise and focused on how things work.
- **Action-Oriented:** Use imperative language in logs and instructions (e.g., "Calibrate pH sensor" instead of "The pH sensor should be calibrated").
- **Consistency:** Use standardized units (°C, mS/cm, pH) throughout all user interfaces and logs.

## UX Principles
- **Real-Time Visibility:** Sensor data should be updated frequently enough to be useful (every 0.5 to 1 second).
- **Status Indicators:** Use clear labels (e.g., "Normal", "High", "Low", "Failed") to represent sensor health and server connectivity.
- **Error Handling:** When a sensor or network fails, provide a specific reason if possible, without cluttering the main data view.

## Visual Identity (CLI/Logs)
- **Structured Output:** Prefer tables or clearly labeled key-value pairs for sensor readings in the console.
- **Visual Feedback:** Use simple ASCII borders and separators to organize data.
- **Minimalist:** Avoid unnecessary conversational filler in the terminal output.

## Operational Standards
- **Calibration:** Sensor calibration values must be stored in external configuration files (`ph_cal.json`) rather than hardcoded in the main script.
- **Connectivity:** Always provide a visual indicator of server communication status.
- **Reliability:** Background processes (like camera streaming) must be managed to prevent resource leaks on the Raspberry Pi.

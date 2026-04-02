# Tech Stack: LeafCloudIoT

## Programming Language
- **Python (3.x):** Primary language for sensor data collection, processing, and streaming.

## Frameworks and Libraries
- **requests:** For sending JSON-formatted sensor data to the remote FastAPI server.
- **adafruit-ads1x15:** Interface library for the ADS1115 analog-to-digital converter.
- **board & busio:** CircuitPython-compatible libraries for I2C and hardware management.
- **statistics:** Used for median filtering to clean noisy sensor data.
- **threading:** For non-blocking management of camera streaming and data collection.

## Hardware & Communication Protocols
- **Raspberry Pi:** The primary compute node for local sensor management.
- **I2C Protocol:** Used for communication with the ADS1115 ADC.
- **1-Wire Protocol:** Used for temperature sensor (DS18B20) communication.
- **UDP (User Datagram Protocol):** Used for low-latency camera streaming via `rpicam-vid`.

## Backend Integration
- **FastAPI:** Remote server (on MacBook) that receives and processes sensor payloads.
- **JSON:** Standard data format for all sensor-to-server communication.

## Operating System & Environment
- **Raspberry Pi OS:** The Linux-based environment running the sensor monitoring scripts.
- **v1-gpio & v1-therm:** Kernel modules for 1-Wire sensor support.

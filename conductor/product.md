# Product Guide: LeafCloudIoT

## # Initial Concept
Monitor and stream water quality sensor data (Temperature, EC, pH) from a Raspberry Pi to a MacBook FastAPI server.

## Overview
LeafCloudIoT is a specialized IoT monitoring solution designed to track environmental and water quality parameters. It leverages the Raspberry Pi's GPIO and I2C capabilities to gather precise data from multiple sensors, providing a real-time stream of information to a centralized dashboard or API.

## Core Vision
To provide a reliable, modular, and easy-to-deploy monitoring system for hydroponic, aquaponic, or general water quality applications, ensuring data accuracy through signal processing and seamless network integration.

## Target Users
- Hydroponic and Aquaponic growers.
- Environmental researchers.
- IoT enthusiasts monitoring water quality at home.

## Key Features
- **Multi-Sensor Integration:** Unified monitoring of Temperature (1-Wire), pH (ADC/A1), and EC (ADC/A0).
- **Signal Processing:** Uses median filtering to eliminate electrical noise and provide stable readings.
- **Real-Time Data Streaming:** Transmits sensor payloads (JSON) to a remote FastAPI endpoint.
- **Active Control Loop:** Only collects and streams sensor data when an active command (bucket_id) is received from the server, reducing unnecessary data generation.
- **Integrated Video Monitoring:** Support for background camera streaming (rpicam-vid) alongside sensor data.
- **Robustness:** Handles network failures and provides clear status updates (e.g., pH/EC out-of-range warnings).

## Design Principles
- **Accuracy First:** Prioritize data integrity via sampling and calibration.
- **Modularity:** Easily add or remove sensors with minimal code changes.
- **Connectivity:** Designed for seamless integration with existing network-based APIs.

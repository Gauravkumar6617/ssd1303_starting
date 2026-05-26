# ESP32 IoT Smart Display Projects

## Overview

This project demonstrates two IoT systems built using ESP32 and a 128x64 OLED display. The system connects to WiFi, fetches live data from online APIs, and displays it on the OLED screen in real time.

The two main projects included are:

1. Smart Weather Display System  
2. Telegram Notification Display System  

---

## Hardware Requirements

- ESP32 microcontroller board  
- 0.96 inch OLED display (SSD1306, 128x64, I2C)  
- Jumper wires  
- Breadboard (optional)  
- USB cable for programming  

---

## Project 1: Smart Weather Display System

### Description

This project displays live weather data on an OLED screen using an internet API. The ESP32 connects to WiFi, fetches weather information, and displays it in real time.

### Features

- WiFi connectivity  
- Live weather data fetching  
- OLED display output  
- Real-time updates  

### Working Flow

WiFi → Weather API → ESP32 → OLED Display  

### Example Output

Lucknow  
Temp: 32°C  
Partly Cloudy  

---

## Project 2: Telegram Notification Display System

### Description

This project uses Telegram Bot API to display incoming messages on an OLED screen connected to ESP32.

### Features

- Telegram Bot integration  
- Real-time message fetching  
- OLED message display  
- Continuous polling system  

### Setup Requirements

- Telegram Bot created using BotFather  
- Bot Token  
- Chat ID  

### Working Flow

Telegram App → Bot API → ESP32 → OLED Display  

### Example Output

Telegram Message:  
Hello ESP32  

---

## Hardware Connections

OLED Display (I2C):

- SDA → GPIO 21  
- SCL → GPIO 22  
- VCC → 3.3V  
- GND → GND  

---

## Technologies Used

- MicroPython  
- ESP32 WiFi  
- REST APIs  
- Telegram Bot API  
- I2C OLED Communication  

---

## Key Learning Outcomes

- Embedded IoT system development  
- API integration with microcontrollers  
- JSON data parsing  
- Real-time data visualization  
- Wireless communication using WiFi  

---

## Future Improvements

- Combined dashboard (Weather + Telegram + Time)  
- Sensor integration (temperature, humidity, air quality)  
- Push notification system  
- Better OLED UI design with animations  
- Cloud-based IoT control system  

---

## Author

Gaurav Kumar

---

## License

This project is open-source and can be used for learning and development purposes.

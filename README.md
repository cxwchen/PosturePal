# PosturePal
A real-time posture monitoring and feedback system using biofeedback, machine learning, and smart notifications.

## Overview
PosturePal is a personal system designed to help improve posture throughout the day. It combines **hardware-based sensing** (EMG and motion sensors), **machine learning**, and **real-time alerts** to encourage better posture habits.


## Current Features
**Pushover Reminders**: Sends notifications to your phone every 5 minutes using the [Pushover API](https://pushover.net/api) to remind you to check and correct your posture.
> **Note**: This interval-based notification system is a temporary solution. Once the hardware arrives, EMG data is collected and a machine learning model is trained, notifications will only be sent when poor posture is detected in real time using the sensor data and classification model.


## Planned Features
### 1. EMG-Based Posture Detection
**Hardware**:
- EMG sensor (MyoWare 2.0)
- Microcontroller: Arduino Nano 33 BLE Sense Rev2

**Functionality**:
- Collect EMG data from target muscles (lower back)
- Extract features
- Perform SVM classification (on-device or on-phone) to detect bad posture
### 2. BLE Integration
The Arduino Nano 33 BLE will transmit data to your phone or computer using Bluetooth Low Energy (BLE) for real-time feedback
### 3. Laptop Overlay App
A desktop app that overlays posture warnings on your screen when bad posture is detected. This helps you stay mindful even while working.
<!-- In the future, I will use EMG sensors in combination with an Arduino Nano 33 BLE Sense rev2 to monitor the EMG signals and extract basic features. These will be sent using BLE to the device and said device performs the classification task (SVM) of poor posture vs good posture. Based on the results, an alert will be sent to me to remind me to fix my posture on my phone.  -->

Additionally, I want to create an application for my laptop. This application has an overlay such that if my posture is bad a message will be printed on my screen to remind me to fix my posture.

## Roadmap
### Phase 1: Basic Reminders (In Progress)
-   [x] Set up Pushover integration for posture reminders on phone
-   [x] Send notifications every 5 minutes
-   [ ] Create lightweight GUI for laptop-based posture prompts

### Phase 2: Hardware Integration (Pending)
-   [ ] Acquire EMG Sensor (MyoWare 2.0)
-   [ ] Acquire Arduino Nano 33 BLE Sense Rev2
-   [ ] Integrate EMG sensor with the Arduino

### Phase 3: Data Acquisition and Machine Learning (Pending)
-   [ ] Collect EMG data for good vs bad posture using serial communication
-   [ ] Extract features and train SVM classifier
-   [ ] Deploy model to device (or run classification on phone/laptop)

### Phase 4: Real-Time Feedback (Pending)
-   [ ] Replace time-based notifications with ML-triggered alerts
-   [ ] Enable real-time classification and notification via Pushover
-   [ ] Test and optimize latency and responsiveness

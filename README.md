# LifeSignal: Elderly Health Monitoring System

## Overview

LifeSignal is an integrated health monitoring system designed to protect elderly users through real-time health tracking and emergency alerts. The system consists of a watchOS app for data collection and an iOS app for data analysis and caregiver monitoring.

## Features

- Real-time health monitoring via Apple Watch
  - Heart rate tracking
  - Blood oxygen monitoring
  - Fall detection
- Remote caregiver dashboard
- QR code/passcode-based device pairing
- Intelligent alert system with customizable thresholds
- Emergency contact notification system

## Technical Requirements

- iOS 15.0 or later
- watchOS 8.0 or later
- Apple Watch Series 6 or later (for blood oxygen monitoring)
- Xcode 13.0 or later
- Swift 5.5 or later

## Project Structure

```
LifeSignal/
├── iOS/                    # iOS app
│   ├── Views/             # SwiftUI views
│   ├── Models/            # Data models
│   ├── Services/          # Business logic and services
│   └── Utils/             # Helper functions and extensions
├── watchOS/               # watchOS app
│   ├── Views/             # Watch interface
│   ├── Models/            # Watch-specific models
│   └── Services/          # Health monitoring services
└── Shared/                # Shared code between iOS and watchOS
    ├── Models/            # Shared data models
    └── Constants/         # Shared constants and configurations
```

## Setup Instructions

1. Clone the repository
2. Open `LifeSignal.xcodeproj` in Xcode
3. Configure signing certificates for both iOS and watchOS targets
4. Build and run the project

## HealthKit Integration

This app requires HealthKit permissions for:

- Heart rate
- Blood oxygen
- Fall detection
- Activity data

## Privacy & Security

- All health data is processed locally on device
- Data transmission uses end-to-end encryption
- Compliant with HIPAA guidelines for health data protection

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Apple HealthKit Documentation
- SwiftUI Framework
# LifeSignal

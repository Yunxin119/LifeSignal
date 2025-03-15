# Development Setup Guide

## Prerequisites

- Xcode 13.0 or later
- Python 3.8 or later
- iOS 15.0 or later (for testing)
- watchOS 8.0 or later (for testing)
- Apple Developer account (for running on real devices)

## Setting Up the Backend Server

1. Navigate to the backend directory:

```bash
cd backend
```

2. Make the setup script executable:

```bash
chmod +x setup.sh
```

3. Run the setup script:

```bash
./setup.sh
```

This will:

- Create a Python virtual environment
- Install required dependencies
- Start the Flask server on localhost:5100

The backend server should now be running and accessible at `http://localhost:5100`.

## Setting Up the iOS/watchOS App

1. Open the Xcode project:

```bash
open LifeSignal.xcodeproj
```

2. Configure Development Team:

   - Select the project in the navigator
   - Select each target (iOS and watchOS)
   - Under Signing & Capabilities, select your development team

3. Configure Network Security:
   - The app is configured to connect to localhost in DEBUG mode
   - For iOS Simulator, localhost connections are allowed by default
   - For real devices, you'll need to use your computer's local IP address

### Running on Real Devices

To test on real devices:

1. Find your computer's local IP address:

```bash
ipconfig getifaddr en0  # For Wi-Fi
# or
ipconfig getifaddr en1  # For Ethernet
```

2. Update the baseURL in `HealthAnalysisService.swift` with your IP:

```swift
#if DEBUG
private let baseURL = "http://YOUR_IP:5100/api"
#else
...
#endif
```

3. Ensure your device is on the same network as your computer

## Testing the Setup

1. Start the backend server (if not already running):

```bash
cd backend
./setup.sh
```

2. Test the API endpoint:

```bash
curl -X POST http://localhost:5100/api/analyze_health_data \
  -H "Content-Type: application/json" \
  -d '{"heart_rate": 75, "blood_oxygen": 98}'
```

3. Run the iOS app in Xcode:

   - Select your target device/simulator
   - Press Cmd+R or click the Run button

4. Test the connection:
   - The app should connect to the local server
   - Check Xcode console for any connection errors
   - Check the Flask server console for incoming requests

## Common Issues

### Network Connection Issues

- Ensure your device and computer are on the same network
- Check if your firewall is blocking connections
- Try using `https` instead of `http` if required by iOS

### HealthKit Permissions

- Real devices require proper provisioning for HealthKit
- Simulator may have limited HealthKit functionality

### Python Environment Issues

- Ensure you have Python 3.8 or later installed
- Check if all dependencies are properly installed
- Try removing and recreating the virtual environment

## Development Workflow

1. Backend Changes:

   - Make changes to Python files
   - Flask will auto-reload in development
   - Test API endpoints using Postman or curl

2. iOS/watchOS Changes:

   - Make changes in Xcode
   - Build and run to test
   - Use Debug console for logging

3. Testing Both:
   - Run backend server
   - Run iOS app
   - Monitor both consoles for issues

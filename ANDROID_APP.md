# WelderTools Android App

WelderTools is now available as a full Android app with a graphical user interface (GUI)!

**📱 New to the app? See [ANDROID_QUICKSTART.md](ANDROID_QUICKSTART.md) for a user-friendly guide!**

## Features

The Android app includes all the functionality of the command-line version:

- **MIG Welding Settings** - Get voltage, wire speed, gas mix recommendations
- **TIG Welding Settings** - Get amperage, tungsten type, polarity guidance
- **Arc/Stick Welding Settings** - Get electrode selection and amperage recommendations
- **Wire Speed Calculator** - Calculate detailed wire speeds by material and wire size
- **Machine Information** - Browse information on major welding machine brands
- **Material Properties** - View composition and weldability data for different metals

## Installation

### Pre-built APK

Download the latest APK from the releases page and install it on your Android device.

### Build from Source

To build the Android app yourself, you'll need:

1. **Linux System** (Ubuntu 20.04+ recommended)
2. **Python 3.8+**
3. **Buildozer** and dependencies

#### Build Steps

1. **Install System Dependencies**
   ```bash
   # Update system
   sudo apt update
   
   # Install build tools
   sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
   
   # Install Cython
   pip3 install --upgrade cython
   ```

2. **Install Buildozer**
   ```bash
   pip3 install --upgrade buildozer
   ```

3. **Clone Repository**
   ```bash
   git clone https://github.com/1090mb/WelderTools.git
   cd WelderTools
   ```

4. **Build APK**
   ```bash
   # First build will take 30-60 minutes as it downloads Android SDK/NDK
   buildozer android release
   ```

5. **Install APK**
   ```bash
   # The APK will be in the bin/ directory
   adb install bin/WelderTools-0.1-release.apk
   
   # Or transfer to your phone and install manually
   ```

## Building Tips

- **First build is slow**: The first build downloads Android SDK, NDK, and all dependencies. This can take 30-60 minutes.
- **Subsequent builds are faster**: After the first build, rebuilds typically take 5-10 minutes.
- **Build cache**: Buildozer caches everything in `.buildozer/` directory. You can delete this to start fresh if you encounter issues.
- **Requirements**: Make sure you have at least 10GB of free disk space for the build environment.

## Troubleshooting

### Build Fails

If the build fails:
1. Delete `.buildozer/` directory
2. Run `buildozer android clean`
3. Try building again

### App Crashes on Startup

- Make sure your device is running Android 5.0 (API 21) or higher
- Check logcat for errors: `adb logcat | grep python`

## Development

The Android app is built with:
- **Kivy** - Cross-platform Python framework
- **Python-for-Android** - Packages Python apps for Android
- **Buildozer** - Build automation tool

Source code:
- `main.py` - GUI application code
- `welder_tools.py` - Core welding expert system
- `weldertools.kv` - Kivy language file for the UI
- `buildozer.spec` - Android build configuration

## License

Same as the main project - see LICENSE file.

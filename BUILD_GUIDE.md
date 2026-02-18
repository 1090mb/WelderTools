# Build Guide

This guide covers building WelderTools for Android and iOS platforms, both locally and via GitHub Actions CI/CD.

## GitHub Actions CI/CD

WelderTools uses automated builds via GitHub Actions for both Android and iOS platforms.

### Automated Release Builds

When you create a new release on GitHub:
1. The workflow automatically triggers
2. Both Android APK and iOS Xcode project are built
3. Build artifacts are automatically attached to the release

**Workflow file**: `.github/workflows/build-and-release.yml`

### Manual Build Trigger

You can also trigger builds manually:
1. Go to Actions tab in GitHub
2. Select "Build and Release APK" workflow
3. Click "Run workflow"
4. Download artifacts from the workflow run

### Key Features of CI/CD Pipeline

- ✅ **Android API 33** - Uses latest stable Android API
- ✅ **JDK 17** - Modern Java runtime
- ✅ **Cython 0.29.36** - Compatible version for both iOS and Android
- ✅ **Automatic SDK License Acceptance** - No manual intervention needed
- ✅ **Build Caching** - Faster subsequent builds
- ✅ **Conditional Uploads** - Releases vs. workflow artifacts

## Local Android Build

### Prerequisites

- Linux System (Ubuntu 20.04+ recommended)
- Python 3.9+
- 8GB+ RAM recommended
- 20GB+ free disk space

### System Dependencies

```bash
sudo apt-get update
sudo apt-get install -y \
    autoconf \
    automake \
    cmake \
    libtool \
    pkg-config \
    libffi-dev \
    libssl-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    libgstreamer1.0-0 \
    libgstreamer1.0-dev \
    libmtdev-dev \
    openjdk-17-jdk
```

### Python Dependencies

```bash
pip install --upgrade pip
pip install buildozer cython==0.29.36 python-for-android
```

### Build APK

```bash
# Set Java home
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Build debug APK
buildozer android debug

# Or build release APK (requires keystore)
buildozer android release
```

The APK will be created in the `bin/` directory.

### Troubleshooting Android Build

**SDK License Issues**:

The Android SDK requires accepting license agreements. This is handled automatically in CI/CD via the `android.accept_sdk_license = True` setting in `buildozer.spec`.

For local builds, create the license file:
```bash
mkdir -p "$HOME/.android"
# This hash represents the Android SDK license agreement
# It may need updating when SDK licenses change
echo -e "\n24333f8a63b6825ea9c5514f83c2829b004d1fee" > "$HOME/.android/repositories.cfg"
```

**Clean Build**:
```bash
buildozer android clean
rm -rf .buildozer
buildozer android debug
```

## Local iOS Build

### Prerequisites

- macOS 11.0+
- Xcode 12.0+
- Python 3.10+
- Homebrew

### System Dependencies

```bash
brew install autoconf automake libtool pkg-config
```

### Python Dependencies

```bash
pip install --upgrade pip
pip install cython==0.29.36
pip install kivy-ios
```

### Build Xcode Project

```bash
# Build dependencies
toolchain build python3 kivy

# Create Xcode project
toolchain create WelderTools .
```

This creates a `WelderTools-ios` directory with an Xcode project.

### Open in Xcode

```bash
cd WelderTools-ios
open WelderTools.xcodeproj
```

Then sign and build the app in Xcode. See [IOS_SIGNING_GUIDE.md](IOS_SIGNING_GUIDE.md) for signing instructions.

## Build Configuration

### buildozer.spec

Key Android build settings:

```ini
[app]
title = WelderTools
package.name = weldertools
package.domain = com.weldertools
version = 0.1
requirements = python3,kivy
orientation = portrait,landscape

# Android configuration
android.permissions = INTERNET
android.api = 33              # Target API level
android.minapi = 21           # Minimum API level
android.ndk = 25b             # NDK version
android.accept_sdk_license = True  # Auto-accept licenses in CI
```

## CI/CD Build Process Details

### Android Build Steps

1. **Checkout code** - Get repository files
2. **Set up Python 3.9** - With pip caching
3. **Cache Buildozer directory** - Speed up subsequent builds
4. **Install system dependencies** - All required libraries
5. **Install Python dependencies** - buildozer, cython, python-for-android
6. **Accept Android SDK Licenses** - Automated license acceptance
7. **Build APK** - Using JDK 17 and buildozer
8. **Upload to Release or Artifacts** - Based on trigger type

### iOS Build Steps

1. **Checkout code** - Get repository files
2. **Set up Python 3.10** - With pip caching
3. **Install dependencies** - cython, kivy-ios, build tools
4. **Build Kivy for iOS** - Compile python3 and kivy
5. **Create Xcode Project** - Generate project structure
6. **Zip Xcode Project** - Package for distribution
7. **Upload to Release or Artifacts** - Based on trigger type

## Version Updates

When updating versions:

1. Update `version = X.Y` in `buildozer.spec`
2. Create a new GitHub release with tag `vX.Y`
3. Workflow automatically builds and attaches artifacts

## Common Issues and Solutions

### Android: "Aidl not found"
- **Cause**: SDK build-tools not installed or license not accepted
- **Solution**: Ensure `android.accept_sdk_license = True` in buildozer.spec

### iOS: "cython is not installed"
- **Cause**: cython must be installed before kivy-ios
- **Solution**: `pip install cython==0.29.36` before kivy-ios

### Both: "Out of memory"
- **Cause**: Insufficient RAM during build
- **Solution**: Close other apps, use machine with 8GB+ RAM

### Android: Java version mismatch
- **Cause**: Wrong Java version
- **Solution**: Use JDK 17, set JAVA_HOME correctly

## Build Artifacts

### Android APK
- **Debug builds**: `bin/weldertools-{version}-armeabi-v7a-debug.apk`
- **Size**: ~20-30 MB
- **Architecture**: ARM 32-bit (armeabi-v7a)

### iOS Xcode Project
- **Package**: `weldertools-ios-project.zip`
- **Size**: ~50-100 MB
- **Contents**: Full Xcode project with dependencies

## Performance Tips

1. **Use cached builds** - Don't clean unless necessary
2. **Parallel builds** - GitHub Actions runs Android and iOS in parallel
3. **Selective builds** - Only build what changed
4. **Local testing** - Test Python code before building mobile apps

## Additional Resources

- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Kivy for iOS Documentation](https://kivy-ios.readthedocs.io/)
- [Android Developer Guide](https://developer.android.com/)
- [iOS Development Guide](https://developer.apple.com/ios/)

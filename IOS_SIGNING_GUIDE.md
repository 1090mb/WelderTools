# iOS Manual Signing Guide

Because the iOS app is built in a cloud environment without your private developer keys, the resulting Xcode project is unsigned. You must sign it manually using Xcode on a Mac to install it on your device.

## Prerequisites

1.  **Mac Computer** with macOS.
2.  **Xcode** installed (free from the Mac App Store).
3.  **Apple ID** (free) or Apple Developer Account.
4.  **iOS Device** (iPhone/iPad) and USB cable.

## Instructions

### 1. Download and Extract
1.  Go to the **Releases** section of the GitHub repository.
2.  Download the `weldertools-ios-project.zip` asset.
3.  Unzip the file. You will see a folder named `WelderTools-ios`.

### 2. Open in Xcode
1.  Open the `WelderTools-ios` folder.
2.  Double-click the `weldertools.xcodeproj` file to open it in Xcode.

### 3. Configure Signing
1.  In the left sidebar (Project Navigator), click the top-level **weldertools** project icon.
2.  In the main view, select the **weldertools** target under "Targets".
3.  Click the **Signing & Capabilities** tab.
4.  Check **Automatically manage signing**.
5.  Select your account in the **Team** dropdown.
    - *If none listed, click "Add an Account..." and log in with your Apple ID.*
6.  If Xcode complains about the Bundle Identifier, change it to something unique (e.g., `com.yourname.weldertools`).

### 4. Build and Install
1.  Connect your iOS device to your Mac via USB.
2.  Unlock your device and tap **Trust** if prompted.
3.  In Xcode's top toolbar, select your device from the destination dropdown (where it might say "Any iOS Device").
4.  Click the **Play** button (Run) or press `Cmd + R`.
5.  Xcode will build the app and install it on your device.

### 5. Trust Developer App (First Run Only)
If you are using a free Apple ID:
1.  On your iOS device, go to **Settings** > **General** > **VPN & Device Management**.
2.  Tap the entry for your email address.
3.  Tap **Trust <your email>** and confirm.

You can now launch WelderTools on your iPhone!
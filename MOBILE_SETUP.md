# WelderTools - Mobile Platform Setup

WelderTools is fully compatible with both Android and iOS platforms. Follow these guides to get started on your mobile device.

---

## Android Setup (Termux)

### What is Termux?
Termux is a powerful terminal emulator for Android that provides a Linux environment without requiring root access.

### Installation Steps

1. **Install Termux**
   - Download from [F-Droid](https://f-droid.org/en/packages/com.termux/) (recommended)
   - Or from [Google Play Store](https://play.google.com/store/apps/details?id=com.termux)

2. **Update Package Lists**
   ```bash
   pkg update && pkg upgrade
   ```

3. **Install Python**
   ```bash
   pkg install python
   ```

4. **Install Git**
   ```bash
   pkg install git
   ```

5. **Clone WelderTools Repository**
   ```bash
   git clone https://github.com/1090mb/WelderTools.git
   cd WelderTools
   ```

6. **Make Executable (Optional)**
   ```bash
   chmod +x welder_tools.py
   ```

### Usage on Android

```bash
# Run commands as usual
python welder_tools.py mig mild_steel 1/8
python welder_tools.py tig aluminum 1/4
python welder_tools.py machine Miller
```

### Android Tips

- **Screen Size**: WelderTools automatically detects mobile platforms and adjusts output formatting for smaller screens
- **Keyboard**: Use Termux's extra keys for special characters (accessible from the keyboard toolbar)
- **Storage Access**: Grant Termux storage permissions to save output to files:
  ```bash
  termux-setup-storage
  ```
- **Keep Screen On**: Enable "Keep screen on while charging" in Developer Options for long-running sessions

---

## iOS Setup

WelderTools supports multiple Python environments on iOS:

### Option 1: Pythonista (Recommended)

**Pythonista** is a complete Python IDE for iOS with a beautiful interface.

1. **Install Pythonista**
   - Download from [App Store](https://apps.apple.com/us/app/pythonista-3/id1085978097)
   - Cost: One-time purchase

2. **Download WelderTools**
   - Option A: Use Pythonista's built-in Git client
   - Option B: Download files manually from GitHub and import into Pythonista

3. **Run WelderTools**
   - Open `welder_tools.py` in Pythonista
   - Use the console to pass arguments:
     ```python
     import sys
     sys.argv = ['welder_tools.py', 'mig', 'mild_steel', '1/8']
     exec(open('welder_tools.py').read())
     ```
   
4. **Create Shortcuts**
   - Save commonly-used commands as separate scripts
   - Add to iOS home screen for quick access

### Option 2: iSH Shell

**iSH** is a Linux shell environment for iOS.

1. **Install iSH**
   - Download from [App Store](https://apps.apple.com/us/app/ish-shell/id1436902243)
   - Free and open-source

2. **Install Python**
   ```bash
   apk add python3
   apk add git
   ```

3. **Clone Repository**
   ```bash
   git clone https://github.com/1090mb/WelderTools.git
   cd WelderTools
   ```

4. **Run WelderTools**
   ```bash
   python3 welder_tools.py mig mild_steel 1/8
   ```

### Option 3: a-Shell

**a-Shell** is another Unix shell for iOS with Python support.

1. **Install a-Shell**
   - Download from [App Store](https://apps.apple.com/us/app/a-shell/id1473805438)
   - Free with optional pro features

2. **Download Repository**
   ```bash
   git clone https://github.com/1090mb/WelderTools.git
   cd WelderTools
   ```

3. **Run Commands**
   ```bash
   python welder_tools.py mig mild_steel 1/8
   ```

### iOS Tips

- **Touch Keyboard**: All iOS Python environments support external keyboard for easier command entry
- **Split View**: Use iOS Split View to reference documentation while running commands
- **Shortcuts Integration**: Create iOS Shortcuts to run common WelderTools commands
- **iCloud Sync**: Some apps support iCloud sync for easy access across devices

---

## Platform Detection

WelderTools automatically detects when it's running on a mobile platform and adjusts the output:

- **Narrower Output**: Text is formatted for smaller screen widths (50 vs 60 characters)
- **Platform Indicator**: Shows which platform you're running on in the header
- **Optimized Formatting**: Section headers and separators are adjusted for mobile viewing

You can verify platform detection by running:
```bash
python welder_tools.py
```

The header will show your current platform.

---

## Common Mobile Commands

Here are quick-reference commands optimized for mobile typing:

### Quick Settings Lookup
```bash
# MIG settings - short material names
python welder_tools.py mig mild_steel 1/8
python welder_tools.py mig aluminum 1/4
python welder_tools.py mig stainless_steel 3/16

# TIG settings
python welder_tools.py tig mild_steel 1/8
python welder_tools.py tig aluminum 1/4

# Stick/Arc settings
python welder_tools.py arc mild_steel 1/4
python welder_tools.py arc stainless_steel 3/16
```

### Machine Information
```bash
# List all brands
python welder_tools.py machine

# Specific brand
python welder_tools.py machine Miller
python welder_tools.py machine Lincoln
```

### Material Properties
```bash
python welder_tools.py material mild_steel
python welder_tools.py material aluminum
python welder_tools.py material stainless_steel
```

---

## Offline Usage

One of the best features for mobile users:

✅ **No Internet Required** - WelderTools works completely offline once installed

✅ **No External Dependencies** - Uses only Python standard library

✅ **Fast Response** - Instant results, no API calls or network delays

✅ **Privacy** - All data stays on your device

This makes WelderTools perfect for use in the shop, garage, or anywhere without reliable internet.

---

## Troubleshooting

### Android (Termux)

**Problem**: "Command not found" error
- **Solution**: Make sure Python is installed: `pkg install python`

**Problem**: Can't clone repository
- **Solution**: Install Git: `pkg install git`

**Problem**: Permission denied
- **Solution**: Run `chmod +x welder_tools.py`

### iOS

**Problem**: Can't find files in Pythonista
- **Solution**: Check the "This iPhone" or "iCloud" section in the file browser

**Problem**: Syntax errors when running
- **Solution**: Make sure you're using the correct argument passing method for your iOS Python environment

**Problem**: iSH commands run slowly
- **Solution**: iSH emulates x86 on ARM, so some slowness is expected. Consider Pythonista for better performance.

---

## Creating Mobile-Friendly Aliases

### Android (Termux)

Create a `.bashrc` file with aliases:

```bash
echo 'alias weld="cd ~/WelderTools && python welder_tools.py"' >> ~/.bashrc
source ~/.bashrc
```

Now you can use:
```bash
weld mig mild_steel 1/8
```

### iOS (Pythonista)

Create wrapper scripts for common operations:

**mig_check.py**:
```python
import sys
sys.argv = ['welder_tools.py', 'mig', 'mild_steel', '1/8']
exec(open('welder_tools.py').read())
```

---

## Feature Parity

✅ **Complete Feature Parity**: All features work identically on mobile and desktop platforms

✅ **Same Commands**: No special mobile syntax needed

✅ **Consistent Output**: Results are the same, just optimized for screen size

✅ **No Limitations**: Full access to all welding data and calculations

---

## Contributing

If you find mobile-specific issues or have suggestions for improving mobile usability, please open an issue on GitHub.

---

## License

MIT License - Same as the main WelderTools project

---

**Need Help?** Check the main README.md or QUICK_REFERENCE.md for detailed welding information and command examples.

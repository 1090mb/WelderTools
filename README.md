# WelderTools

![WelderTools Tests](https://github.com/1090mb/WelderTools/actions/workflows/python-app.yml/badge.svg)
![Build and Release APK](https://github.com/1090mb/WelderTools/actions/workflows/build-and-release.yml/badge.svg)

**Professional Welding Assistant** - Expert guidance on MIG, TIG, and Arc welding with comprehensive knowledge base.

The best welder assistant in the world. Knows everything about welding: MIG, TIG, Arc. All the machines, tools, brands, parts, and components. All the settings, temperatures, and wire speeds. Provides straightforward, no-nonsense output.

**✨ Now available as a native Android app!** Full GUI interface for your phone or tablet.

## Platforms Supported

- ✅ **Android** - Native GUI app

**Cross-Platform**: Android GUI app uses Kivy framework.

## Features

- **MIG Welding Settings**: Voltage, wire speed, gas mix, wire size for mild steel, stainless, and aluminum
- **TIG Welding Settings**: Amperage, tungsten type, polarity, gas flow for all materials
- **Arc/Stick Welding Settings**: Electrode selection, amperage, polarity for various applications
- **Wire Speed Calculator**: Detailed wire speed recommendations by material and wire size
- **Machine Knowledge**: Information on major brands (Miller, Lincoln, ESAB, Hobart, Everlast, Fronius)
- **Material Properties**: Composition, weldability, and special considerations for different metals
- **Session Tracking**: Log welding hours and parts. Export logs to CSV.

## Running the Application

### Prerequisites
- Python 3.6+
- Kivy

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/1090mb/WelderTools.git
    cd WelderTools
    ```

2.  **Install dependencies:**
    ```bash
    pip install kivy
    ```

### Running the App

```bash
python main.py
```

## Building the APK

This project is set up to be built into an Android APK using [Buildozer](https://buildozer.readthedocs.io/en/latest/).

1.  **Install Buildozer:**
    ```bash
    pip install buildozer
    ```

2.  **Build the APK:**
    ```bash
    buildozer android debug
    ```
    The APK will be created in the `bin/` directory.

### iOS (Manual)

1.  Download the `weldertools-ios-project.zip` from the GitHub Release.
2.  Unzip and open `weldertools.xcodeproj` in Xcode on a Mac.
3.  Follow the iOS Manual Signing Guide to sign and install the app.

## Testing

Run the included test suite to verify functionality:

```bash
python test_welder_tools.py
python test_android_app.py
```

## Releasing the App

To release the app, you need to create a new release on GitHub. This will trigger the `build-and-release` workflow, which will build the app and upload the APK to the release.

## Usage

The application provides a user-friendly interface to access all the features of WelderTools.
- Select the welding process (MIG, TIG, Arc).
- Choose the material and thickness.
- Get instant settings and recommendations.
- Browse information about welding machines and materials.

## Supported Materials

- **Mild Steel**: Most common, easiest to weld
- **Stainless Steel**: 304, 316, 309 grades
- **Aluminum**: 6061, 5052, 7075 alloys
- **Cast Iron**: Repair welding with nickel rods

## Supported Thicknesses

- `1/16"` - Thin material
- `1/8"` - Light gauge
- `3/16"` - Medium thickness
- `1/4"` - Heavy gauge
- `3/8"` - Thick material (Arc only)

## Key Principles

### MIG Welding
- **Travel Speed**: 8-12 IPM for most applications
- **Stick Out**: 3/8 to 1/2 inch from contact tip
- **Gas Flow**: 15-25 CFH depending on conditions
- **Wire Size**: Larger wire for thicker material

### TIG Welding
- **Polarity**: DCEN for steel, AC for aluminum
- **Tungsten**: Lanthanated/Ceriated for DC (safer than thoriated), Pure/Zirconated for AC
- **Gas**: 100% Argon for most applications
- **Amperage**: Rule of thumb: 1 amp per 0.001" thickness

### Arc/Stick Welding
- **E6010**: Deep penetration, all position, DCEP
- **E7018**: Low hydrogen, smooth bead, AC or DCEP
- **Arc Length**: Keep tight, about electrode diameter
- **Travel Angle**: 5-15 degrees drag angle

## Tips for Success

1. **Clean your material** - Remove rust, paint, oil, and oxidation
2. **Check your gas** - Ensure proper flow and no leaks
3. **Practice travel speed** - Too fast = narrow bead, too slow = slag inclusion
4. **Watch the puddle** - It tells you everything about heat input
5. **Use the right filler** - Match base metal or use appropriate filler
6. **Safety first** - Proper ventilation, PPE, and fire prevention

## Common Issues

### MIG Welding
- **Porosity**: Check gas flow, clean material, check for drafts
- **Spatter**: Reduce voltage, increase wire speed slightly
- **Burn-through**: Lower heat, increase travel speed
- **Cold lap**: Increase heat, slow down travel speed

### TIG Welding
- **Tungsten contamination**: Use proper amperage, don't dip tungsten
- **Porosity**: Check gas coverage, clean material thoroughly
- **Uneven bead**: Work on consistent travel speed and torch angle
- **Cracking**: Control heat input, use proper filler metal

### Arc/Stick Welding
- **Stick electrode**: Arc too long, reduce amperage
- **Undercut**: Too much amperage, too fast travel
- **Overlap**: Too slow travel, too low amperage
- **Slag inclusion**: Clean between passes, proper technique

## License

MIT License - See LICENSE file for details.

## Contributing

Contributions welcome! This tool is designed to help welders with accurate, professional information.

## Disclaimer

Always follow manufacturer's recommendations and safety guidelines. This tool provides general guidance based on industry standards. Actual settings may vary based on specific conditions, equipment, and application requirements.

# WelderTools

**Professional Welding Assistant** - Expert guidance on MIG, TIG, and Arc welding with comprehensive knowledge base.

The best welder assistant in the world. Knows everything about welding: MIG, TIG, Arc. All the machines, tools, brands, parts, and components. All the settings, temperatures, and wire speeds. Provides straightforward, no-nonsense output.

**✨ Now with full Android and iOS support!** Use WelderTools on your phone or tablet in the shop. See [MOBILE_SETUP.md](MOBILE_SETUP.md) for details.

## Platforms Supported

- ✅ **Linux** - Full support
- ✅ **macOS** - Full support  
- ✅ **Windows** - Full support
- ✅ **Android** - Full support via Termux
- ✅ **iOS** - Full support via Pythonista, iSH, or a-Shell

**Cross-Platform**: Pure Python with no external dependencies - works everywhere Python 3.6+ runs!

## Features

- **MIG Welding Settings**: Voltage, wire speed, gas mix, wire size for mild steel, stainless, and aluminum
- **TIG Welding Settings**: Amperage, tungsten type, polarity, gas flow for all materials
- **Arc/Stick Welding Settings**: Electrode selection, amperage, polarity for various applications
- **Wire Speed Calculator**: Detailed wire speed recommendations by material and wire size
- **Machine Knowledge**: Information on major brands (Miller, Lincoln, ESAB, Hobart, Everlast, Fronius)
- **Material Properties**: Composition, weldability, and special considerations for different metals
- **Hours & Parts Tracking**: Log welding sessions, track hours worked and parts made, view statistics

## Installation

### Desktop (Linux, macOS, Windows)

No installation required. Just Python 3.x.

```bash
# Clone the repository
git clone <repository_url>
cd WelderTools

# Make executable (optional, Unix-like systems)
chmod +x welder_tools.py
```

### Mobile Platforms

For detailed mobile setup instructions:
- **Android (Termux)**: See [MOBILE_SETUP.md](MOBILE_SETUP.md#android-setup-termux)
- **iOS (Pythonista/iSH)**: See [MOBILE_SETUP.md](MOBILE_SETUP.md#ios-setup)

Quick mobile setup:
```bash
# Android (Termux) or iOS (iSH/a-Shell)
pkg install python git  # or: apk add python3 git
git clone <repository_url>
cd WelderTools
python welder_tools.py mig mild_steel 1/8
```

## Usage

### MIG Welding Settings

```bash
python welder_tools.py mig <material> <thickness>
```

**Examples:**
```bash
# Mild steel, 1/8" thick
python welder_tools.py mig mild_steel 1/8

# Stainless steel, 3/16" thick
python welder_tools.py mig stainless_steel 3/16

# Aluminum, 1/4" thick
python welder_tools.py mig aluminum 1/4
```

**Output includes:**
- Voltage range
- Wire speed (IPM)
- Gas mixture
- Wire size
- Travel speed
- Stick out distance

### TIG Welding Settings

```bash
python welder_tools.py tig <material> <thickness>
```

**Examples:**
```bash
# Mild steel, 1/8" thick
python welder_tools.py tig mild_steel 1/8

# Aluminum, 1/4" thick (AC TIG)
python welder_tools.py tig aluminum 1/4

# Stainless steel, 3/16" thick
python welder_tools.py tig stainless_steel 3/16
```

**Output includes:**
- Amperage range
- Tungsten type and size
- Polarity (AC/DCEN)
- Gas flow rate
- Frequency and balance (for aluminum)
- Special notes

### Arc/Stick Welding Settings

```bash
python welder_tools.py arc <material> <thickness>
```

**Examples:**
```bash
# Mild steel, 1/4" thick
python welder_tools.py arc mild_steel 1/4

# Stainless steel, 3/16" thick
python welder_tools.py arc stainless_steel 3/16

# Cast iron repair
python welder_tools.py arc cast_iron
```

**Output includes:**
- Electrode type and size
- Amperage range
- Polarity (AC/DC)
- Travel angle
- Arc length
- Special techniques

### Wire Speed Recommendations

```bash
python welder_tools.py wire <material> <wire_size> <thickness_category>
```

**Examples:**
```bash
# Mild steel, 0.035" wire, medium thickness
python welder_tools.py wire mild_steel 0.035 medium

# Aluminum, 3/64" wire, thick material
python welder_tools.py wire aluminum 3/64 thick

# Stainless steel, 0.030" wire, thin material
python welder_tools.py wire stainless_steel 0.030 thin
```

**Thickness categories:** `thin`, `medium`, `thick`, `very_thick`

### Machine Information

```bash
python welder_tools.py machine [brand]
```

**Examples:**
```bash
# List all brands
python welder_tools.py machine

# Get info on specific brand
python welder_tools.py machine Miller
python welder_tools.py machine Lincoln
python welder_tools.py machine ESAB
```

**Brands covered:**
- Miller (Dynasty, Syncrowave, Millermatic)
- Lincoln (PowerMIG, Square Wave, Tombstone)
- ESAB (Rebel, Caddy)
- Hobart (Handler, IronMan)
- Everlast (PowerTIG, PowerMTS)
- Fronius (TransPocket, MagicWave)

### Material Properties

```bash
python welder_tools.py material <material>
```

**Examples:**
```bash
python welder_tools.py material mild_steel
python welder_tools.py material aluminum
python welder_tools.py material stainless_steel
python welder_tools.py material cast_iron
```

**Output includes:**
- Composition
- Weldability rating
- Preheat requirements
- Special concerns
- Preparation steps
- Common uses

### Hours & Parts Tracking

Track your welding work with built-in session logging:

```bash
# Log a welding session
python welder_tools.py log <hours> <parts> [description]

# View recent log entries
python welder_tools.py view [limit]

# View statistics
python welder_tools.py stats

# Clear all log entries
python welder_tools.py clear
```

**Examples:**
```bash
# Log 4.5 hours with 12 parts made and a description
python welder_tools.py log 4.5 12 "Welded steel brackets for truck bed"

# Log session without description
python welder_tools.py log 2.5 7

# View last 20 entries
python welder_tools.py view 20

# View all statistics
python welder_tools.py stats
```

**Tracking data includes:**
- Date and time of each session
- Hours worked
- Number of parts made
- Optional description
- Cumulative statistics (total hours, total parts, averages)

All tracking data is stored locally in `welding_log.json` and persists between sessions.

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

---

## Mobile Users

📱 **Using on Android or iOS?** Check out [MOBILE_SETUP.md](MOBILE_SETUP.md) for platform-specific setup guides, tips, and troubleshooting.

**Mobile Features:**
- ✅ Offline operation - no internet required
- ✅ Optimized output for smaller screens
- ✅ All features work identically to desktop
- ✅ Quick access in the shop on your phone or tablet

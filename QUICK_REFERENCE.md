# WelderTools Quick Reference Guide

## Common Welding Settings at a Glance

### MIG Welding - Mild Steel
| Thickness | Voltage | Wire Speed | Wire Size | Gas Mix |
|-----------|---------|------------|-----------|---------|
| 1/16"     | 16-18V  | 200-300 IPM | 0.023"   | C25 (75/25) |
| 1/8"      | 17-19V  | 250-350 IPM | 0.030"   | C25 (75/25) |
| 3/16"     | 18-21V  | 300-400 IPM | 0.035"   | C25 (75/25) |
| 1/4"      | 20-23V  | 350-450 IPM | 0.045"   | C25 (75/25) |

### TIG Welding - Aluminum (AC)
| Thickness | Amperage | Tungsten Type | Frequency |
|-----------|----------|---------------|-----------|
| 1/16"     | 60-90A   | Pure/Zirc 1/16" | 60-120 Hz |
| 1/8"      | 100-130A | Pure/Zirc 3/32" | 60-120 Hz |
| 3/16"     | 140-180A | Pure/Zirc 1/8"  | 60-120 Hz |
| 1/4"      | 190-240A | Pure/Zirc 1/8"  | 60-120 Hz |

### Arc/Stick Welding - Mild Steel
| Thickness | Electrode | Amperage | Polarity |
|-----------|-----------|----------|----------|
| 1/8"      | 1/8" E7018 | 90-120A | AC/DCEP |
| 3/16"     | 5/32" E7018 | 110-150A | AC/DCEP |
| 1/4"      | 3/16" E7018 | 140-190A | AC/DCEP |
| 3/8"      | 1/4" E7018 | 180-250A | AC/DCEP |

## Essential Gas Mixtures

- **C25 (75% Ar / 25% CO2)**: Mild steel MIG - most common
- **100% Argon**: TIG all materials, aluminum MIG
- **98% Ar / 2% CO2**: Stainless steel MIG
- **90% Ar / 10% CO2**: Heavy steel fabrication

## Tungsten Selection Guide

### DC Applications (Steel, Stainless)
- **2% Lanthanated (Blue)**: Best all-around, safe alternative to thoriated
- **2% Ceriated (Orange)**: Good for low amperage, safe
- **Avoid Thoriated (Red/Yellow)**: Old standard, radioactive, health concerns

### AC Applications (Aluminum)
- **Pure (Green)**: Traditional choice, requires ball end
- **Zirconated (White/Brown)**: More durable, better arc stability

## Electrode Selection Guide

- **E6010**: Deep penetration, all-position, dirty metal, DCEP only
- **E6011**: Like 6010 but AC capable
- **E7018**: Low hydrogen, smooth bead, critical welds, AC or DCEP
- **E308L-16**: Stainless steel, low carbon
- **ENi-CI**: Cast iron repair, nickel rod

## Wire Speed Rules of Thumb

### By Material (0.035" wire, medium thickness)
- **Mild Steel**: 300-400 IPM
- **Stainless Steel**: 280-380 IPM  
- **Aluminum**: 350-450 IPM

### Adjustment Tips
- **Porosity?** Increase wire speed 50-75 IPM
- **Burn-through?** Decrease wire speed 50-75 IPM
- **Too cold?** Increase voltage 1-2V or decrease speed
- **Too hot?** Decrease voltage 1-2V or increase speed

## Heat Input Guidelines

### Preheat Requirements
- **Mild Steel**: Only if thick (>3/8") or very cold
- **Stainless**: Generally no preheat (causes distortion)
- **Aluminum**: No preheat (except heavy casting repair)
- **Cast Iron**: 200-400°F preheat mandatory

### Interpass Temperature
- **Mild Steel**: Keep below 500°F to avoid grain growth
- **Stainless**: Keep below 350°F to prevent sensitization
- **Aluminum**: Can weld hot, watch for meltdown
- **Cast Iron**: Keep below 200°F, slow cooling

## Common Problems and Fixes

### MIG Welding
| Problem | Cause | Fix |
|---------|-------|-----|
| Porosity | Contamination, no gas | Clean metal, check gas flow (15-25 CFH) |
| Spatter | Voltage too high | Reduce voltage 1-2V, check ground |
| Bird nesting | Drive rolls tension | Adjust tension, check liner |
| Burn-through | Too much heat | Lower voltage, faster travel |

### TIG Welding
| Problem | Cause | Fix |
|---------|-------|-----|
| Gray/Black weld | Contamination | Increase gas flow, check coverage |
| Tungsten in weld | Dipping/touching | Re-grind, increase amperage |
| Cracking | Wrong filler | Use correct filler metal |
| Porosity | Dirty base | Clean with acetone/stainless brush |

### Stick Welding
| Problem | Cause | Fix |
|---------|-------|-----|
| Sticking | Too low amperage | Increase amperage 10-20A |
| Undercut | Too fast/hot | Slow down, reduce amperage |
| Slag inclusion | Dirty weld | Clean between passes, proper angle |
| Porosity | Damp rods | Dry rods in oven (250°F for 2 hours) |

## Safety Checklist

- [ ] Proper ventilation (especially stainless, galvanized)
- [ ] Welding helmet with proper shade (10-13)
- [ ] Leather gloves and jacket
- [ ] Fire extinguisher nearby
- [ ] Remove flammables from area
- [ ] Check gas cylinder secured
- [ ] Ground clamp properly attached
- [ ] Inspect cables for damage
- [ ] Dry electrodes (stick welding)
- [ ] Clean metal surface

## Material Preparation

### Mild Steel
1. Remove rust, scale, paint with grinder
2. Clean with wire brush
3. Degrease if oily

### Stainless Steel
1. Remove any contamination
2. Clean with **stainless wire brush only** (not carbon steel)
3. Degrease with acetone
4. Avoid fingerprints (oils cause porosity)

### Aluminum
1. Remove oxide layer with **stainless wire brush**
2. Clean with acetone or denatured alcohol
3. Weld immediately (oxide reforms quickly)
4. Never use carbon steel brush (embeds iron)

### Cast Iron
1. Clean thoroughly (grinder, wire brush)
2. Preheat to 200-400°F
3. Weld short beads (1-2")
4. Peen while hot
5. Slow cool (bury in sand)

## Recommended Machines by Use Case

### Home/Hobby (<$1000)
- **Hobart Handler 140/190**: Great entry-level MIG
- **Everlast PowerTIG 200DV**: Budget TIG, dual voltage
- **Lincoln AC-225**: Classic stick welder

### Professional Single-Process ($1000-2500)
- **Miller Millermatic 211**: Professional MIG
- **Miller Dynasty 210**: Industry-standard TIG
- **Lincoln Tombstone**: Bulletproof stick welder

### Multi-Process ($1500-3000)
- **Miller Multimatic 220**: MIG/TIG/Stick combo
- **ESAB Rebel EMP 215ic**: Excellent multi-process
- **Lincoln Power MIG 210 MP**: Versatile multi-process

### Industrial (>$3000)
- **Fronius TransSteel**: Top-tier MIG
- **Miller Dynasty 350**: Heavy-duty TIG
- **Lincoln Flextec 650**: Advanced multi-process

 
---
**Note**: These are general guidelines. Always adjust for specific conditions, equipment, and application requirements. When in doubt, run test beads on scrap material.

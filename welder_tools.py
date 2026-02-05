#!/usr/bin/env python3
"""
WelderTools - Professional Welding Assistant
Expert guidance on MIG, TIG, Arc welding with comprehensive knowledge base
"""

class WeldingExpert:
    """Expert system for all welding processes and equipment"""
    
    def __init__(self):
        self.mig_settings = self._init_mig_settings()
        self.tig_settings = self._init_tig_settings()
        self.arc_settings = self._init_arc_settings()
        self.wire_speeds = self._init_wire_speeds()
        self.machine_brands = self._init_machine_brands()
        self.materials = self._init_materials()
    
    def _init_mig_settings(self):
        """Initialize MIG welding parameters"""
        return {
            'mild_steel': {
                'thickness_range': {
                    '1/16': {'voltage': '16-18V', 'wire_speed': '200-300 IPM', 'gas': '75% Ar / 25% CO2', 'wire_size': '0.023"'},
                    '1/8': {'voltage': '17-19V', 'wire_speed': '250-350 IPM', 'gas': '75% Ar / 25% CO2', 'wire_size': '0.030"'},
                    '3/16': {'voltage': '18-21V', 'wire_speed': '300-400 IPM', 'gas': '75% Ar / 25% CO2', 'wire_size': '0.035"'},
                    '1/4': {'voltage': '20-23V', 'wire_speed': '350-450 IPM', 'gas': '75% Ar / 25% CO2', 'wire_size': '0.045"'},
                },
                'travel_speed': '8-12 IPM',
                'stick_out': '3/8 to 1/2 inch'
            },
            'stainless_steel': {
                'thickness_range': {
                    '1/16': {'voltage': '16-18V', 'wire_speed': '180-280 IPM', 'gas': '98% Ar / 2% CO2', 'wire_size': '0.030"'},
                    '1/8': {'voltage': '17-20V', 'wire_speed': '230-330 IPM', 'gas': '98% Ar / 2% CO2', 'wire_size': '0.035"'},
                    '3/16': {'voltage': '19-22V', 'wire_speed': '280-380 IPM', 'gas': '98% Ar / 2% CO2', 'wire_size': '0.035"'},
                    '1/4': {'voltage': '21-24V', 'wire_speed': '330-430 IPM', 'gas': '98% Ar / 2% CO2', 'wire_size': '0.045"'},
                }
            },
            'aluminum': {
                'thickness_range': {
                    '1/16': {'voltage': '17-19V', 'wire_speed': '300-400 IPM', 'gas': '100% Ar', 'wire_size': '0.030"'},
                    '1/8': {'voltage': '18-21V', 'wire_speed': '350-450 IPM', 'gas': '100% Ar', 'wire_size': '0.035"'},
                    '3/16': {'voltage': '20-23V', 'wire_speed': '400-500 IPM', 'gas': '100% Ar', 'wire_size': '3/64"'},
                    '1/4': {'voltage': '22-25V', 'wire_speed': '450-550 IPM', 'gas': '100% Ar', 'wire_size': '3/64"'},
                },
                'notes': 'Use spool gun or push-pull system. Clean surface thoroughly.'
            }
        }
    
    def _init_tig_settings(self):
        """Initialize TIG welding parameters"""
        return {
            'mild_steel': {
                'thickness_range': {
                    '1/16': {'amperage': '40-60A', 'tungsten': '1/16" 2% Thoriated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '1/8': {'amperage': '70-90A', 'tungsten': '3/32" 2% Thoriated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '3/16': {'amperage': '100-130A', 'tungsten': '1/8" 2% Thoriated', 'gas': '100% Ar', 'flow_rate': '15-25 CFH'},
                    '1/4': {'amperage': '140-180A', 'tungsten': '1/8" 2% Thoriated', 'gas': '100% Ar', 'flow_rate': '20-25 CFH'},
                },
                'polarity': 'DCEN (DC Electrode Negative)',
                'notes': 'Add filler rod as needed'
            },
            'stainless_steel': {
                'thickness_range': {
                    '1/16': {'amperage': '40-60A', 'tungsten': '1/16" 2% Lanthanated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '1/8': {'amperage': '70-95A', 'tungsten': '3/32" 2% Lanthanated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '3/16': {'amperage': '105-140A', 'tungsten': '1/8" 2% Lanthanated', 'gas': '100% Ar', 'flow_rate': '15-25 CFH'},
                    '1/4': {'amperage': '150-190A', 'tungsten': '1/8" 2% Lanthanated', 'gas': '100% Ar', 'flow_rate': '20-25 CFH'},
                },
                'polarity': 'DCEN (DC Electrode Negative)',
                'notes': 'Backpurge on critical applications'
            },
            'aluminum': {
                'thickness_range': {
                    '1/16': {'amperage': '60-90A', 'tungsten': '1/16" Pure or Zirconated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '1/8': {'amperage': '100-130A', 'tungsten': '3/32" Pure or Zirconated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '3/16': {'amperage': '140-180A', 'tungsten': '1/8" Pure or Zirconated', 'gas': '100% Ar', 'flow_rate': '20-25 CFH'},
                    '1/4': {'amperage': '190-240A', 'tungsten': '1/8" Pure or Zirconated', 'gas': '100% Ar', 'flow_rate': '20-30 CFH'},
                },
                'polarity': 'AC (Alternating Current)',
                'frequency': '60-120 Hz for optimal cleaning',
                'balance': '70% EN / 30% EP for cleaning action',
                'notes': 'Clean with stainless brush and acetone'
            }
        }
    
    def _init_arc_settings(self):
        """Initialize Arc/Stick welding parameters"""
        return {
            'mild_steel': {
                'thickness_range': {
                    '1/8': {'electrode': '1/8" E6010 or E7018', 'amperage': '90-120A', 'polarity': 'DCEP (E6010) or AC (E7018)'},
                    '3/16': {'electrode': '5/32" E7018', 'amperage': '110-150A', 'polarity': 'AC or DCEP'},
                    '1/4': {'electrode': '3/16" E7018', 'amperage': '140-190A', 'polarity': 'AC or DCEP'},
                    '3/8': {'electrode': '1/4" E7018', 'amperage': '180-250A', 'polarity': 'AC or DCEP'},
                },
                'travel_angle': '5-15 degrees drag',
                'arc_length': 'Tight arc (electrode diameter)'
            },
            'stainless_steel': {
                'thickness_range': {
                    '1/8': {'electrode': '1/8" E308L-16', 'amperage': '85-115A', 'polarity': 'DCEP'},
                    '3/16': {'electrode': '5/32" E308L-16', 'amperage': '105-145A', 'polarity': 'DCEP'},
                    '1/4': {'electrode': '3/16" E308L-16', 'amperage': '135-185A', 'polarity': 'DCEP'},
                },
                'notes': 'Keep heat input low to prevent sensitization'
            },
            'cast_iron': {
                'electrode': 'ENi-CI (Nickel)',
                'preheat': '200-400°F',
                'technique': 'Short beads (1-2 inches), peening, slow cooling',
                'notes': 'Keep interpass temp below 200°F'
            }
        }
    
    def _init_wire_speeds(self):
        """Wire speed recommendations by material and wire size"""
        return {
            'mild_steel': {
                '0.023': {'thin': '200-300 IPM', 'medium': '250-350 IPM'},
                '0.030': {'thin': '250-350 IPM', 'medium': '300-400 IPM', 'thick': '350-450 IPM'},
                '0.035': {'medium': '300-400 IPM', 'thick': '350-500 IPM'},
                '0.045': {'thick': '350-550 IPM', 'very_thick': '400-600 IPM'},
            },
            'stainless_steel': {
                '0.030': {'thin': '230-330 IPM', 'medium': '280-380 IPM'},
                '0.035': {'medium': '280-380 IPM', 'thick': '330-430 IPM'},
                '0.045': {'thick': '330-480 IPM'},
            },
            'aluminum': {
                '0.030': {'thin': '300-400 IPM', 'medium': '350-450 IPM'},
                '0.035': {'medium': '350-450 IPM', 'thick': '400-500 IPM'},
                '3/64': {'thick': '400-550 IPM', 'very_thick': '450-600 IPM'},
            }
        }
    
    def _init_machine_brands(self):
        """Major welding equipment brands and their specialties"""
        return {
            'Miller': {
                'popular_models': ['Millermatic 211', 'Dynasty 210', 'Syncrowave 210', 'Diversion 180'],
                'specialty': 'Professional grade, excellent TIG machines',
                'reputation': 'Industry standard, highly reliable'
            },
            'Lincoln': {
                'popular_models': ['PowerMIG 210 MP', 'Square Wave TIG 200', 'Tombstone AC225', 'Precision TIG 225'],
                'specialty': 'Wide range, strong stick welders',
                'reputation': 'Workhorse machines, great value'
            },
            'ESAB': {
                'popular_models': ['Rebel EMP 215ic', 'Caddy Tig 2200i', 'Warrior 500i'],
                'specialty': 'Multi-process machines, industrial equipment',
                'reputation': 'Innovative, European quality'
            },
            'Hobart': {
                'popular_models': ['Handler 190', 'IronMan 230', 'Stickmate 160i'],
                'specialty': 'Hobbyist to professional, value-oriented',
                'reputation': 'Reliable, good entry-level machines'
            },
            'Everlast': {
                'popular_models': ['PowerTIG 210EXT', 'PowerMTS 211Si', 'Lightning MTS 275'],
                'specialty': 'Budget multi-process, inverter technology',
                'reputation': 'Good value, improving quality'
            },
            'Fronius': {
                'popular_models': ['TransPocket 180', 'MagicWave 230i', 'TransSteel 2200'],
                'specialty': 'Premium industrial, advanced technology',
                'reputation': 'Top-tier quality, expensive'
            }
        }
    
    def _init_materials(self):
        """Material properties and welding considerations"""
        return {
            'mild_steel': {
                'composition': 'Low carbon steel (< 0.3% carbon)',
                'weldability': 'Excellent',
                'preheat': 'Not required unless thick or cold',
                'common_uses': 'Structural, automotive, general fabrication'
            },
            'stainless_steel': {
                'composition': 'Iron + Chromium (10.5%+) + Nickel',
                'weldability': 'Good with proper filler',
                'concerns': 'Distortion, carbide precipitation, heat control',
                'grades': {
                    '304': 'Most common, general purpose',
                    '316': 'Marine grade, better corrosion resistance',
                    '309': 'Dissimilar metal filler'
                }
            },
            'aluminum': {
                'composition': 'Pure aluminum or alloys (6061, 5052, 7075)',
                'weldability': 'Moderate - requires AC TIG or MIG with spool gun',
                'concerns': 'Oxide layer, heat conductivity, distortion',
                'preparation': 'Remove oxide with stainless brush, clean with acetone'
            },
            'cast_iron': {
                'composition': 'Iron + high carbon (2-4%)',
                'weldability': 'Difficult - brittle, cracks easily',
                'technique': 'Nickel rods, preheat, short beads, slow cool',
                'notes': 'Often better to braze than weld'
            }
        }
    
    def get_mig_settings(self, material, thickness):
        """Get MIG welding settings for material and thickness"""
        material = material.lower().replace(' ', '_')
        if material not in self.mig_settings:
            return f"Material '{material}' not found. Available: {', '.join(self.mig_settings.keys())}"
        
        mat_data = self.mig_settings[material]
        if thickness not in mat_data['thickness_range']:
            available = ', '.join(mat_data['thickness_range'].keys())
            return f"Thickness '{thickness}' not found for {material}. Available: {available}"
        
        settings = mat_data['thickness_range'][thickness]
        output = f"\n=== MIG WELDING - {material.upper().replace('_', ' ')} - {thickness}\" ===\n"
        output += f"Voltage: {settings['voltage']}\n"
        output += f"Wire Speed: {settings['wire_speed']}\n"
        output += f"Gas: {settings['gas']}\n"
        output += f"Wire Size: {settings['wire_size']}\n"
        
        if 'travel_speed' in mat_data:
            output += f"Travel Speed: {mat_data['travel_speed']}\n"
        if 'stick_out' in mat_data:
            output += f"Stick Out: {mat_data['stick_out']}\n"
        if 'notes' in mat_data:
            output += f"Notes: {mat_data['notes']}\n"
        
        return output
    
    def get_tig_settings(self, material, thickness):
        """Get TIG welding settings for material and thickness"""
        material = material.lower().replace(' ', '_')
        if material not in self.tig_settings:
            return f"Material '{material}' not found. Available: {', '.join(self.tig_settings.keys())}"
        
        mat_data = self.tig_settings[material]
        if thickness not in mat_data['thickness_range']:
            available = ', '.join(mat_data['thickness_range'].keys())
            return f"Thickness '{thickness}' not found for {material}. Available: {available}"
        
        settings = mat_data['thickness_range'][thickness]
        output = f"\n=== TIG WELDING - {material.upper().replace('_', ' ')} - {thickness}\" ===\n"
        output += f"Amperage: {settings['amperage']}\n"
        output += f"Tungsten: {settings['tungsten']}\n"
        output += f"Gas: {settings['gas']}\n"
        output += f"Flow Rate: {settings['flow_rate']}\n"
        output += f"Polarity: {mat_data['polarity']}\n"
        
        if 'frequency' in mat_data:
            output += f"Frequency: {mat_data['frequency']}\n"
        if 'balance' in mat_data:
            output += f"Balance: {mat_data['balance']}\n"
        if 'notes' in mat_data:
            output += f"Notes: {mat_data['notes']}\n"
        
        return output
    
    def get_arc_settings(self, material, thickness):
        """Get Arc/Stick welding settings for material and thickness"""
        material = material.lower().replace(' ', '_')
        if material not in self.arc_settings:
            return f"Material '{material}' not found. Available: {', '.join(self.arc_settings.keys())}"
        
        mat_data = self.arc_settings[material]
        
        # Cast iron is special case
        if material == 'cast_iron':
            output = f"\n=== ARC/STICK WELDING - CAST IRON ===\n"
            output += f"Electrode: {mat_data['electrode']}\n"
            output += f"Preheat: {mat_data['preheat']}\n"
            output += f"Technique: {mat_data['technique']}\n"
            output += f"Notes: {mat_data['notes']}\n"
            return output
        
        if thickness not in mat_data['thickness_range']:
            available = ', '.join(mat_data['thickness_range'].keys())
            return f"Thickness '{thickness}' not found for {material}. Available: {available}"
        
        settings = mat_data['thickness_range'][thickness]
        output = f"\n=== ARC/STICK WELDING - {material.upper().replace('_', ' ')} - {thickness}\" ===\n"
        output += f"Electrode: {settings['electrode']}\n"
        output += f"Amperage: {settings['amperage']}\n"
        output += f"Polarity: {settings['polarity']}\n"
        
        if 'travel_angle' in mat_data:
            output += f"Travel Angle: {mat_data['travel_angle']}\n"
        if 'arc_length' in mat_data:
            output += f"Arc Length: {mat_data['arc_length']}\n"
        if 'notes' in mat_data:
            output += f"Notes: {mat_data['notes']}\n"
        
        return output
    
    def get_machine_info(self, brand=None):
        """Get information about welding machine brands"""
        if brand is None:
            output = "\n=== WELDING MACHINE BRANDS ===\n\n"
            for brand_name, info in self.machine_brands.items():
                output += f"{brand_name}:\n"
                output += f"  Specialty: {info['specialty']}\n"
                output += f"  Reputation: {info['reputation']}\n"
                output += f"  Popular Models: {', '.join(info['popular_models'])}\n\n"
            return output
        
        brand = brand.title()
        if brand not in self.machine_brands:
            return f"Brand '{brand}' not found. Available: {', '.join(self.machine_brands.keys())}"
        
        info = self.machine_brands[brand]
        output = f"\n=== {brand.upper()} WELDING MACHINES ===\n"
        output += f"Specialty: {info['specialty']}\n"
        output += f"Reputation: {info['reputation']}\n"
        output += f"Popular Models:\n"
        for model in info['popular_models']:
            output += f"  - {model}\n"
        
        return output
    
    def get_material_info(self, material):
        """Get information about welding materials"""
        material = material.lower().replace(' ', '_')
        if material not in self.materials:
            return f"Material '{material}' not found. Available: {', '.join(self.materials.keys())}"
        
        info = self.materials[material]
        output = f"\n=== {material.upper().replace('_', ' ')} ===\n"
        output += f"Composition: {info['composition']}\n"
        output += f"Weldability: {info['weldability']}\n"
        
        if 'preheat' in info:
            output += f"Preheat: {info['preheat']}\n"
        if 'concerns' in info:
            output += f"Concerns: {info['concerns']}\n"
        if 'preparation' in info:
            output += f"Preparation: {info['preparation']}\n"
        if 'technique' in info:
            output += f"Technique: {info['technique']}\n"
        if 'common_uses' in info:
            output += f"Common Uses: {info['common_uses']}\n"
        if 'grades' in info:
            output += "Grades:\n"
            for grade, desc in info['grades'].items():
                output += f"  {grade}: {desc}\n"
        if 'notes' in info:
            output += f"Notes: {info['notes']}\n"
        
        return output
    
    def get_wire_speed(self, material, wire_size, thickness_category):
        """Get wire speed recommendations"""
        material = material.lower().replace(' ', '_')
        if material not in self.wire_speeds:
            return f"Material '{material}' not found. Available: {', '.join(self.wire_speeds.keys())}"
        
        mat_data = self.wire_speeds[material]
        if wire_size not in mat_data:
            available = ', '.join(mat_data.keys())
            return f"Wire size '{wire_size}' not found for {material}. Available: {available}"
        
        wire_data = mat_data[wire_size]
        if thickness_category not in wire_data:
            available = ', '.join(wire_data.keys())
            return f"Thickness category '{thickness_category}' not found. Available: {available}"
        
        speed = wire_data[thickness_category]
        output = f"\n=== WIRE SPEED - {material.upper().replace('_', ' ')} ===\n"
        output += f"Wire Size: {wire_size}\"\n"
        output += f"Thickness: {thickness_category}\n"
        output += f"Wire Speed: {speed}\n"
        
        return output


def main():
    """Main CLI interface"""
    import sys
    
    expert = WeldingExpert()
    
    print("=" * 60)
    print("WELDERTOOLS - Professional Welding Assistant")
    print("Expert guidance on MIG, TIG, Arc welding")
    print("=" * 60)
    
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python welder_tools.py mig <material> <thickness>")
        print("  python welder_tools.py tig <material> <thickness>")
        print("  python welder_tools.py arc <material> <thickness>")
        print("  python welder_tools.py wire <material> <wire_size> <thickness_category>")
        print("  python welder_tools.py machine [brand]")
        print("  python welder_tools.py material <material>")
        print("\nExamples:")
        print("  python welder_tools.py mig mild_steel 1/8")
        print("  python welder_tools.py tig aluminum 1/4")
        print("  python welder_tools.py arc stainless_steel 3/16")
        print("  python welder_tools.py wire mild_steel 0.035 medium")
        print("  python welder_tools.py machine Miller")
        print("  python welder_tools.py material aluminum")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'mig' and len(sys.argv) >= 4:
        material = sys.argv[2]
        thickness = sys.argv[3]
        print(expert.get_mig_settings(material, thickness))
    
    elif command == 'tig' and len(sys.argv) >= 4:
        material = sys.argv[2]
        thickness = sys.argv[3]
        print(expert.get_tig_settings(material, thickness))
    
    elif command == 'arc' and len(sys.argv) >= 4:
        material = sys.argv[2]
        thickness = sys.argv[3]
        print(expert.get_arc_settings(material, thickness))
    
    elif command == 'wire' and len(sys.argv) >= 5:
        material = sys.argv[2]
        wire_size = sys.argv[3]
        thickness = sys.argv[4]
        print(expert.get_wire_speed(material, wire_size, thickness))
    
    elif command == 'machine':
        brand = sys.argv[2] if len(sys.argv) >= 3 else None
        print(expert.get_machine_info(brand))
    
    elif command == 'material' and len(sys.argv) >= 3:
        material = sys.argv[2]
        print(expert.get_material_info(material))
    
    else:
        print(f"\nInvalid command or missing arguments.")
        print("Run without arguments to see usage.")


if __name__ == "__main__":
    main()

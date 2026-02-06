#!/usr/bin/env python3
"""
WelderTools - Professional Welding Assistant
Expert guidance on MIG, TIG, Arc welding with comprehensive knowledge base
Cross-platform support: Desktop, Android (Termux), iOS (Pythonista/iSH)
"""

import sys
import platform
import os
import json
from datetime import datetime


def get_platform_info():
    """Detect current platform and return platform-specific information"""
    system = platform.system()
    
    # Detect Android (Termux)
    if 'ANDROID_ROOT' in os.environ or 'ANDROID_DATA' in os.environ:
        return {
            'name': 'Android',
            'mobile': True,
            'terminal_width': 50,  # Mobile screen width
            'note': 'Running on Android (Termux)'
        }
    
    # Detect iOS (check for common iOS Python environments: Pythonista, iSH, a-Shell)
    is_ios = (system == 'Darwin' and 
              ('Pythonista' in sys.executable or 
               'iSH' in os.environ.get('SHELL', '') or
               'a-Shell' in sys.executable or
               'LC_TERMINAL' in os.environ and os.environ.get('LC_TERMINAL') == 'a-Shell'))
    
    if is_ios:
        return {
            'name': 'iOS',
            'mobile': True,
            'terminal_width': 50,  # Mobile screen width
            'note': 'Running on iOS'
        }
    
    # Desktop platforms
    return {
        'name': system,
        'mobile': False,
        'terminal_width': 60,  # Desktop screen width
        'note': f'Running on {system}'
    }


class WeldingExpert:
    """Expert system for all welding processes and equipment"""
    
    def __init__(self, log_file='welding_log.json'):
        self.mig_settings = self._init_mig_settings()
        self.tig_settings = self._init_tig_settings()
        self.arc_settings = self._init_arc_settings()
        self.wire_speeds = self._init_wire_speeds()
        self.machine_brands = self._init_machine_brands()
        self.materials = self._init_materials()
        self.platform_info = get_platform_info()
        self.log_file = log_file
    
    def _format_header(self, text):
        """Format header based on platform (mobile-friendly for smaller screens)"""
        if self.platform_info['mobile']:
            # Shorter separator for mobile
            return f"\n{'=' * 50}\n{text}\n{'=' * 50}\n"
        else:
            return f"\n{'=' * 60}\n{text}\n{'=' * 60}\n"
    
    def _format_section(self, title):
        """Format section title based on platform"""
        return f"\n=== {title} ===\n"
    
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
                    '1/16': {'amperage': '40-60A', 'tungsten': '1/16" 2% Lanthanated or Ceriated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '1/8': {'amperage': '70-90A', 'tungsten': '3/32" 2% Lanthanated or Ceriated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '3/16': {'amperage': '100-130A', 'tungsten': '1/8" 2% Lanthanated or Ceriated', 'gas': '100% Ar', 'flow_rate': '15-25 CFH'},
                    '1/4': {'amperage': '140-180A', 'tungsten': '1/8" 2% Lanthanated or Ceriated', 'gas': '100% Ar', 'flow_rate': '20-25 CFH'},
                },
                'polarity': 'DCEN (DC Electrode Negative)',
                'notes': 'Add filler rod as needed. Lanthanated/Ceriated tungsten preferred over thoriated.'
            },
            'stainless_steel': {
                'thickness_range': {
                    '1/16': {'amperage': '40-60A', 'tungsten': '1/16" 2% Lanthanated or Ceriated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '1/8': {'amperage': '70-95A', 'tungsten': '3/32" 2% Lanthanated or Ceriated', 'gas': '100% Ar', 'flow_rate': '15-20 CFH'},
                    '3/16': {'amperage': '105-140A', 'tungsten': '1/8" 2% Lanthanated or Ceriated', 'gas': '100% Ar', 'flow_rate': '15-25 CFH'},
                    '1/4': {'amperage': '150-190A', 'tungsten': '1/8" 2% Lanthanated or Ceriated', 'gas': '100% Ar', 'flow_rate': '20-25 CFH'},
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
        output = self._format_section(f"MIG WELDING - {material.upper().replace('_', ' ')} - {thickness}\"")
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
        output = self._format_section(f"TIG WELDING - {material.upper().replace('_', ' ')} - {thickness}\"")
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
            output = self._format_section("ARC/STICK WELDING - CAST IRON")
            output += f"Electrode: {mat_data['electrode']}\n"
            output += f"Preheat: {mat_data['preheat']}\n"
            output += f"Technique: {mat_data['technique']}\n"
            output += f"Notes: {mat_data['notes']}\n"
            return output
        
        if thickness not in mat_data['thickness_range']:
            available = ', '.join(mat_data['thickness_range'].keys())
            return f"Thickness '{thickness}' not found for {material}. Available: {available}"
        
        settings = mat_data['thickness_range'][thickness]
        output = self._format_section(f"ARC/STICK WELDING - {material.upper().replace('_', ' ')} - {thickness}\"")
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
            output = self._format_section("WELDING MACHINE BRANDS")
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
        output = self._format_section(f"{brand.upper()} WELDING MACHINES")
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
        output = self._format_section(material.upper().replace('_', ' '))
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
        output = self._format_section(f"WIRE SPEED - {material.upper().replace('_', ' ')}")
        output += f"Wire Size: {wire_size}\"\n"
        output += f"Thickness: {thickness_category}\n"
        output += f"Wire Speed: {speed}\n"
        
        return output
    
    def _load_log(self):
        """Load tracking log from JSON file"""
        if not os.path.exists(self.log_file):
            return []
        try:
            with open(self.log_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    
    def _save_log(self, log_data):
        """Save tracking log to JSON file"""
        try:
            with open(self.log_file, 'w') as f:
                json.dump(log_data, f, indent=2)
            return True
        except IOError:
            return False
    
    def log_session(self, hours, parts, description=''):
        """Log a welding session with hours worked and parts made"""
        log_data = self._load_log()
        
        entry = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'hours': float(hours),
            'parts': int(parts),
            'description': description
        }
        
        log_data.append(entry)
        
        if self._save_log(log_data):
            output = self._format_section("SESSION LOGGED")
            output += f"Date: {entry['date']}\n"
            output += f"Time: {entry['time']}\n"
            output += f"Hours: {entry['hours']}\n"
            output += f"Parts Made: {entry['parts']}\n"
            if description:
                output += f"Description: {description}\n"
            return output
        else:
            return "Error: Could not save log data"
    
    def view_log(self, limit=10):
        """View recent log entries"""
        log_data = self._load_log()
        
        if not log_data:
            return "No log entries found"
        
        # Show most recent entries first
        recent_entries = log_data[-limit:]
        recent_entries.reverse()
        
        output = self._format_section(f"RECENT LOG ENTRIES (Last {min(limit, len(log_data))})")
        
        for entry in recent_entries:
            output += f"\nDate: {entry['date']} {entry['time']}\n"
            output += f"  Hours: {entry['hours']}\n"
            output += f"  Parts: {entry['parts']}\n"
            if entry.get('description'):
                output += f"  Description: {entry['description']}\n"
        
        return output
    
    def get_stats(self):
        """Get statistics on logged hours and parts"""
        log_data = self._load_log()
        
        if not log_data:
            return "No log entries found"
        
        total_hours = sum(entry['hours'] for entry in log_data)
        total_parts = sum(entry['parts'] for entry in log_data)
        total_sessions = len(log_data)
        avg_hours = total_hours / total_sessions if total_sessions > 0 else 0
        avg_parts = total_parts / total_sessions if total_sessions > 0 else 0
        
        output = self._format_section("WELDING STATISTICS")
        output += f"Total Sessions: {total_sessions}\n"
        output += f"Total Hours: {total_hours:.2f}\n"
        output += f"Total Parts Made: {total_parts}\n"
        output += f"Average Hours/Session: {avg_hours:.2f}\n"
        output += f"Average Parts/Session: {avg_parts:.1f}\n"
        
        return output
    
    def clear_log(self):
        """Clear all log entries"""
        if self._save_log([]):
            return self._format_section("LOG CLEARED") + "All log entries have been removed\n"
        else:
            return "Error: Could not clear log data"


def main():
    """Main CLI interface"""
    import sys
    
    expert = WeldingExpert()
    platform_info = expert.platform_info
    
    # Use platform-aware separator
    sep_len = 50 if platform_info['mobile'] else 60
    separator = "=" * sep_len
    
    print(separator)
    print("WELDERTOOLS - Professional Welding Assistant")
    print("Expert guidance on MIG, TIG, Arc welding")
    if platform_info['mobile']:
        print(f"Platform: {platform_info['note']}")
    print(separator)
    
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python welder_tools.py mig <material> <thickness>")
        print("  python welder_tools.py tig <material> <thickness>")
        print("  python welder_tools.py arc <material> <thickness>")
        print("  python welder_tools.py wire <material> <wire_size> <thickness_category>")
        print("  python welder_tools.py machine [brand]")
        print("  python welder_tools.py material <material>")
        print("\nTracking:")
        print("  python welder_tools.py log <hours> <parts> [description]")
        print("  python welder_tools.py view [limit]")
        print("  python welder_tools.py stats")
        print("  python welder_tools.py clear")
        print("\nExamples:")
        print("  python welder_tools.py mig mild_steel 1/8")
        print("  python welder_tools.py tig aluminum 1/4")
        print("  python welder_tools.py arc stainless_steel 3/16")
        print("  python welder_tools.py wire mild_steel 0.035 medium")
        print("  python welder_tools.py machine Miller")
        print("  python welder_tools.py material aluminum")
        print("  python welder_tools.py log 4.5 12 'Welded steel brackets'")
        print("  python welder_tools.py view 20")
        print("  python welder_tools.py stats")
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
    
    elif command == 'log' and len(sys.argv) >= 4:
        hours = sys.argv[2]
        parts = sys.argv[3]
        description = ' '.join(sys.argv[4:]) if len(sys.argv) > 4 else ''
        print(expert.log_session(hours, parts, description))
    
    elif command == 'view':
        limit = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
        print(expert.view_log(limit))
    
    elif command == 'stats':
        print(expert.get_stats())
    
    elif command == 'clear':
        print(expert.clear_log())
    
    else:
        print(f"\nInvalid command or missing arguments.")
        print("Run without arguments to see usage.")


if __name__ == "__main__":
    main()

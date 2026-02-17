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
import csv
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

    def log_session(self, hours, parts, notes=""):
        """Log a welding session"""
        entry = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'hours': float(hours),
            'parts': int(parts),
            'notes': notes
        }
        
        try:
            data = []
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r') as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = []
            
            data.append(entry)
            
            with open(self.log_file, 'w') as f:
                json.dump(data, f, indent=4)
                
            msg = f"Session logged: {hours} hours, {parts} parts"
            if notes:
                msg += f" - {notes}"
            return msg
        except Exception as e:
            return f"Error logging session: {e}"

    def view_log(self, limit=5):
        """View recent log entries"""
        if not os.path.exists(self.log_file):
            return "No log entries found."
            
        try:
            with open(self.log_file, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    return "Log file is empty or corrupted."
            
            if not data:
                return "No log entries found."
                
            output = self._format_section(f"WELDING LOG (Last {limit})")
            
            # Sort by date descending
            # Reverse list first so that stable sort keeps later entries (newer) first when dates are equal
            data.reverse()
            data.sort(key=lambda x: x.get('date', ''), reverse=True)
            
            for entry in data[:limit]:
                output += f"Date: {entry.get('date', 'N/A')}\n"
                output += f"Duration: {entry.get('hours', 0)} hours\n"
                output += f"Parts: {entry.get('parts', 0)}\n"
                if entry.get('notes'):
                    output += f"Notes: {entry.get('notes')}\n"
                output += "-" * 30 + "\n"
                
            return output
        except Exception as e:
            return f"Error reading log: {e}"

    def get_stats(self):
        """Get statistics from log"""
        if not os.path.exists(self.log_file):
            return "No log entries found."
            
        try:
            with open(self.log_file, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    return "Log file is empty or corrupted."
            
            if not data:
                return "No log entries found."
                
            total_sessions = len(data)
            total_hours = sum(entry.get('hours', 0) for entry in data)
            total_parts = sum(entry.get('parts', 0) for entry in data)
            
            output = self._format_section("WELDING STATISTICS")
            output += f"Total Sessions: {total_sessions}\n"
            output += f"Total Hours: {total_hours:.2f}\n"
            output += f"Total Parts Made: {total_parts}\n"
            if total_sessions > 0:
                output += f"Avg Hours/Session: {total_hours/total_sessions:.2f}\n"
            
            return output
        except Exception as e:
            return f"Error calculating stats: {e}"

    def clear_log(self):
        """Clear the log file"""
        try:
            with open(self.log_file, 'w') as f:
                json.dump([], f)
            return "CLEARED"
        except Exception as e:
            return f"Error clearing log: {e}"

    def export_log_to_csv(self, filename='welding_log_export.csv'):
        """Export the welding log to a CSV file"""
        if not os.path.exists(self.log_file):
            return "No log entries found to export."
            
        try:
            with open(self.log_file, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    return "Log file is empty or corrupted."
            
            if not data:
                return "No log entries found to export."
                
            # Standard fields for the CSV
            fieldnames = ['date', 'hours', 'parts', 'notes']
            
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for entry in data:
                    # Ensure we only write known fields and handle missing ones
                    row = {field: entry.get(field, '') for field in fieldnames}
                    writer.writerow(row)
                    
            return f"Log exported to {filename}"
        except Exception as e:
            return f"Error exporting log: {e}"

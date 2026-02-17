#!/usr/bin/env python3
"""
Test script for WelderTools Android app
Tests the basic structure without requiring a display
"""

import sys
import os
import ast

def test_file_structure():
    """Test that all required files exist"""
    print("Testing file structure...")
    
    required_files = [
        'main.py',
        'welder_tools.py',
        'buildozer.spec',
        'ANDROID_APP.md',
        'README.md'
    ]
    
    all_exist = True
    for filename in required_files:
        if os.path.exists(filename):
            print(f"✓ {filename} exists")
        else:
            print(f"✗ {filename} not found")
            all_exist = False
    
    return all_exist


def test_main_py_structure():
    """Test that main.py has the required structure"""
    print("\nTesting main.py structure...")
    
    try:
        with open('main.py', 'r') as f:
            content = f.read()
        
        # Parse the AST
        tree = ast.parse(content)
        
        # Get all class names
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        
        required_classes = [
            'WelderToolsApp',
            'MainMenuScreen',
            'WeldingSettingsScreen',
            'WireSpeedScreen',
            'MachineInfoScreen',
            'MaterialScreen',
            'TrackingScreen'
        ]
        
        for cls_name in required_classes:
            if cls_name in classes:
                print(f"✓ {cls_name} class found")
            else:
                print(f"✗ {cls_name} class not found")
                return False
        
        # Check for Kivy imports
        if 'from kivy.app import App' in content:
            print("✓ Kivy imports present")
        else:
            print("✗ Kivy imports missing")
            return False
        
        # Check for welder_tools import
        if 'from welder_tools import WeldingExpert' in content:
            print("✓ WeldingExpert import present")
        else:
            print("✗ WeldingExpert import missing")
            return False
        
        # Check for export_log method
        if 'def export_log(self):' in content:
            print("✓ export_log method found")
        else:
            print("✗ export_log method missing")
            return False

        return True
    except Exception as e:
        print(f"✗ Failed to parse main.py: {e}")
        return False


def test_welding_expert():
    """Test that WeldingExpert works correctly"""
    print("\nTesting WeldingExpert integration...")
    
    try:
        from welder_tools import WeldingExpert
        expert = WeldingExpert()
        
        # Test MIG settings
        result = expert.get_mig_settings('mild_steel', '1/8')
        if 'MIG WELDING' in result and 'Voltage' in result:
            print("✓ MIG settings working")
        else:
            print("✗ MIG settings not working correctly")
            return False
        
        # Test TIG settings
        result = expert.get_tig_settings('aluminum', '1/4')
        if 'TIG WELDING' in result and 'Amperage' in result:
            print("✓ TIG settings working")
        else:
            print("✗ TIG settings not working correctly")
            return False
        
        # Test Arc settings
        result = expert.get_arc_settings('mild_steel', '1/4')
        if 'ARC' in result.upper() or 'STICK' in result.upper():
            print("✓ Arc settings working")
        else:
            print("✗ Arc settings not working correctly")
            return False
        
        # Test wire speed
        result = expert.get_wire_speed('mild_steel', '0.035', 'medium')
        if 'WIRE SPEED' in result.upper():
            print("✓ Wire speed calculator working")
        else:
            print("✗ Wire speed calculator not working correctly")
            return False
        
        # Test machine info
        result = expert.get_machine_info('Miller')
        if 'MILLER' in result.upper():
            print("✓ Machine info working")
        else:
            print("✗ Machine info not working correctly")
            return False
        
        # Test material info
        result = expert.get_material_info('aluminum')
        if 'ALUMINUM' in result.upper():
            print("✓ Material info working")
        else:
            print("✗ Material info not working correctly")
            return False
        
        return True
    except Exception as e:
        print(f"✗ Failed to test WeldingExpert: {e}")
        return False


def test_buildozer_spec():
    """Test that buildozer.spec exists and has correct settings"""
    print("\nTesting buildozer.spec...")
    
    if not os.path.exists('buildozer.spec'):
        print("✗ buildozer.spec not found")
        return False
    
    print("✓ buildozer.spec exists")
    
    with open('buildozer.spec', 'r') as f:
        content = f.read()
        
        checks = [
            ('title = WelderTools', 'App title'),
            ('package.name = weldertools', 'Package name'),
            ('package.domain = com.weldertools', 'Package domain'),
            ('requirements = python3,kivy', 'Requirements'),
            ('orientation = portrait,landscape', 'Orientation'),
        ]
        
        for check, desc in checks:
            if check in content:
                print(f"✓ {desc} configured correctly")
            else:
                print(f"✗ {desc} not configured correctly")
                return False
    
    return True


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("WelderTools Android App Tests")
    print("=" * 60)
    
    results = []
    
    # Test file structure
    results.append(("File Structure", test_file_structure()))
    
    # Test main.py structure
    results.append(("Main.py Structure", test_main_py_structure()))
    
    # Test WeldingExpert
    results.append(("WeldingExpert Integration", test_welding_expert()))
    
    # Test buildozer.spec
    results.append(("Buildozer Configuration", test_buildozer_spec()))
    
    # Print summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\nAll tests passed! The Android app is ready to build.")
        print("\nTo build the Android app, run:")
        print("  buildozer android debug")
        return 0
    else:
        print(f"\nFAILED: {total - passed} test(s) failed. Please fix the issues.")
        return 1


if __name__ == '__main__':
    sys.exit(run_all_tests())

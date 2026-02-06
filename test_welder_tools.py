#!/usr/bin/env python3
"""
Tests for WelderTools
Validates welding parameter calculations and settings
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from welder_tools import WeldingExpert, get_platform_info


def test_platform_detection():
    """Test platform detection functionality"""
    platform_info = get_platform_info()
    
    # Verify platform info has required keys
    assert 'name' in platform_info
    assert 'mobile' in platform_info
    assert 'terminal_width' in platform_info
    assert 'note' in platform_info
    
    # Verify mobile is boolean
    assert isinstance(platform_info['mobile'], bool)
    
    # Verify terminal_width is appropriate (50 for mobile, 60 for desktop)
    assert platform_info['terminal_width'] in [50, 60]
    
    print(f"✓ Platform detection works: {platform_info['note']}")


def test_mobile_formatting():
    """Test that mobile formatting methods work"""
    expert = WeldingExpert()
    
    # Verify platform info is stored
    assert hasattr(expert, 'platform_info')
    assert expert.platform_info is not None
    
    # Test formatting methods
    header = expert._format_header("Test Header")
    assert "Test Header" in header
    assert "===" in header
    
    section = expert._format_section("Test Section")
    assert "Test Section" in section
    assert "===" in section
    
    print("✓ Mobile formatting methods work correctly")


def test_mig_settings():
    """Test MIG welding settings retrieval"""
    expert = WeldingExpert()
    
    # Test mild steel
    result = expert.get_mig_settings('mild_steel', '1/8')
    assert '17-19V' in result
    assert '250-350 IPM' in result
    assert '75% Ar / 25% CO2' in result
    print("✓ MIG mild steel settings correct")
    
    # Test aluminum
    result = expert.get_mig_settings('aluminum', '1/4')
    assert '22-25V' in result
    assert '100% Ar' in result
    print("✓ MIG aluminum settings correct")
    
    # Test stainless
    result = expert.get_mig_settings('stainless_steel', '3/16')
    assert '19-22V' in result
    assert '98% Ar / 2% CO2' in result
    print("✓ MIG stainless steel settings correct")


def test_tig_settings():
    """Test TIG welding settings retrieval"""
    expert = WeldingExpert()
    
    # Test mild steel
    result = expert.get_tig_settings('mild_steel', '1/8')
    assert '70-90A' in result
    assert 'DCEN' in result
    print("✓ TIG mild steel settings correct")
    
    # Test aluminum
    result = expert.get_tig_settings('aluminum', '1/4')
    assert '190-240A' in result
    assert 'AC' in result
    assert '60-120 Hz' in result
    print("✓ TIG aluminum settings correct")
    
    # Test stainless
    result = expert.get_tig_settings('stainless_steel', '3/16')
    assert '105-140A' in result
    assert 'Lanthanated or Ceriated' in result
    print("✓ TIG stainless steel settings correct")


def test_arc_settings():
    """Test Arc/Stick welding settings retrieval"""
    expert = WeldingExpert()
    
    # Test mild steel
    result = expert.get_arc_settings('mild_steel', '1/4')
    assert '140-190A' in result
    assert 'E7018' in result
    print("✓ Arc mild steel settings correct")
    
    # Test stainless
    result = expert.get_arc_settings('stainless_steel', '3/16')
    assert '105-145A' in result
    assert 'E308L-16' in result
    print("✓ Arc stainless steel settings correct")
    
    # Test cast iron
    result = expert.get_arc_settings('cast_iron', '')
    assert 'ENi-CI' in result
    assert '200-400°F' in result
    print("✓ Arc cast iron settings correct")


def test_wire_speeds():
    """Test wire speed calculations"""
    expert = WeldingExpert()
    
    # Test mild steel
    result = expert.get_wire_speed('mild_steel', '0.035', 'medium')
    assert '300-400 IPM' in result
    print("✓ Wire speed mild steel correct")
    
    # Test aluminum
    result = expert.get_wire_speed('aluminum', '3/64', 'thick')
    assert '400-550 IPM' in result
    print("✓ Wire speed aluminum correct")
    
    # Test stainless
    result = expert.get_wire_speed('stainless_steel', '0.030', 'thin')
    assert '230-330 IPM' in result
    print("✓ Wire speed stainless steel correct")


def test_machine_info():
    """Test machine brand information"""
    expert = WeldingExpert()
    
    # Test specific brand
    result = expert.get_machine_info('Miller')
    assert 'Millermatic 211' in result
    assert 'Dynasty 210' in result
    print("✓ Miller machine info correct")
    
    # Test all brands
    result = expert.get_machine_info()
    assert 'Miller' in result
    assert 'Lincoln' in result
    assert 'ESAB' in result
    assert 'Hobart' in result
    print("✓ All machine brands info correct")


def test_material_info():
    """Test material properties"""
    expert = WeldingExpert()
    
    # Test mild steel
    result = expert.get_material_info('mild_steel')
    assert 'Low carbon steel' in result
    assert 'Excellent' in result
    print("✓ Mild steel material info correct")
    
    # Test aluminum
    result = expert.get_material_info('aluminum')
    assert '6061' in result
    assert 'Moderate' in result
    print("✓ Aluminum material info correct")
    
    # Test stainless
    result = expert.get_material_info('stainless_steel')
    assert 'Chromium' in result
    assert '304' in result
    print("✓ Stainless steel material info correct")


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Running WelderTools Tests")
    print("=" * 60)
    print()
    
    try:
        test_platform_detection()
        print()
        test_mobile_formatting()
        print()
        test_mig_settings()
        print()
        test_tig_settings()
        print()
        test_arc_settings()
        print()
        test_wire_speeds()
        print()
        test_machine_info()
        print()
        test_material_info()
        print()
        print("=" * 60)
        print("✓ ALL TESTS PASSED")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print()
        print("=" * 60)
        print(f"✗ TEST FAILED: {e}")
        print("=" * 60)
        return 1
    except Exception as e:
        print()
        print("=" * 60)
        print(f"✗ ERROR: {e}")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())

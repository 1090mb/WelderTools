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


def test_tracking():
    """Test tracking functionality"""
    import tempfile
    import os
    
    # Use temporary file for testing
    fd, temp_path = tempfile.mkstemp(suffix='.json')
    os.close(fd)  # Close the file descriptor immediately
    
    try:
        expert = WeldingExpert(log_file=temp_path)
        
        # Test logging sessions
        result = expert.log_session(3.5, 10, 'Test session 1')
        assert '3.5' in result
        assert '10' in result
        assert 'Test session 1' in result
        print("✓ Log session with description works")
        
        result = expert.log_session(2.0, 5)
        assert '2.0' in result
        assert '5' in result
        print("✓ Log session without description works")
        
        # Test view log
        result = expert.view_log()
        assert '3.5' in result
        assert '2.0' in result
        assert '10' in result
        assert '5' in result
        print("✓ View log works")
        
        # Test view with limit
        result = expert.view_log(limit=1)
        assert '2.0' in result, f"Expected '2.0' (latest session) in result, got:\n{result}"
        assert 'Last 1' in result, "Expected 'Last 1' in header"
        print("✓ View log with limit works (Sort order verified)")
        
        # Test statistics
        result = expert.get_stats()
        assert 'Total Sessions: 2' in result
        assert '5.50' in result  # Total hours
        assert 'Total Parts Made: 15' in result
        print("✓ Statistics calculation works")
        
        # Test clear log
        result = expert.clear_log()
        assert 'CLEARED' in result
        print("✓ Clear log works")
        
        # Verify log is empty after clear
        result = expert.view_log()
        assert 'No log entries' in result
        print("✓ Log is empty after clear")
        
    finally:
        # Clean up temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

def test_csv_export():
    """Test CSV export functionality"""
    import tempfile
    import csv
    
    # Use temporary files
    fd_log, log_path = tempfile.mkstemp(suffix='.json')
    os.close(fd_log)
    
    fd_csv, csv_path = tempfile.mkstemp(suffix='.csv')
    os.close(fd_csv)
    
    try:
        expert = WeldingExpert(log_file=log_path)
        
        # Log some data
        expert.log_session(1.5, 10, "Notes 1")
        expert.log_session(2.5, 20, "Notes 2")
        
        # Export to CSV
        result = expert.export_log_to_csv(csv_path)
        assert f"Log exported to {csv_path}" in result
        
        # Verify CSV content
        with open(csv_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
            assert len(rows) == 2
            assert rows[0]['hours'] == '1.5'
            assert rows[0]['parts'] == '10'
            assert rows[0]['notes'] == 'Notes 1'
            assert rows[1]['hours'] == '2.5'
            
        print("✓ CSV export works correctly")
        
    finally:
        if os.path.exists(log_path):
            os.remove(log_path)
        if os.path.exists(csv_path):
            os.remove(csv_path)

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
        test_tracking()
        print()
        test_csv_export()
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

#!/usr/bin/env python3
"""
Example usage of BMC CPAP Analyzer
Shows how to customize the analysis for your specific data
"""

from bmc_cpap_analyzer import BMCCPAPAnalyzer

def example_basic_usage():
    """Basic usage example"""
    print("=== BASIC USAGE ===")

    # Create analyzer (auto-detects device ID)
    analyzer = BMCCPAPAnalyzer()

    # Run analysis for last 3 months
    analyzer.run_analysis(months=3)

def example_custom_reference_data():
    """Example with custom mobile app reference data"""
    print("\n=== CUSTOM REFERENCE DATA ===")

    # Create analyzer
    analyzer = BMCCPAPAnalyzer("23804346")

    # Update with your mobile app data
    analyzer.mobile_reference = {
        'ahi': 2.1,                    # Your AHI from mobile app
        'avg_pressure': 7.5,           # Your average pressure
        'p95_pressure': 9.0,           # Your 95th percentile pressure
        'min_pressure': 6.0,           # Your min pressure setting
        'max_pressure': 15.0,          # Your max pressure setting
        'avg_leak': 4.2,               # Your average leak rate
        'usage_days_percent': 65.3,    # Your usage percentage
        'usage_4h_percent': 58.7       # Your compliant days percentage
    }

    # Run analysis
    analyzer.run_analysis(months=6)  # Analyze last 6 months

def example_different_timeframes():
    """Example analyzing different timeframes"""
    print("\n=== DIFFERENT TIMEFRAMES ===")

    analyzer = BMCCPAPAnalyzer()

    # Analyze last 3 months
    print("Analyzing last 3 months...")
    analyzer.run_analysis(months=3)

    # Analyze last 6 months
    print("\nAnalyzing last 6 months...")
    analyzer.run_analysis(months=6)

    # Analyze full dataset
    print("\nAnalyzing full dataset...")
    analyzer.run_analysis(months=12)

def example_correlation_interpretation():
    """Example showing how to interpret correlation results"""
    print("\n=== CORRELATION INTERPRETATION ===")

    analyzer = BMCCPAPAnalyzer()

    # Get data without running full analysis
    files = analyzer.get_recent_files(months=3)
    pressures, file_stats = analyzer.extract_pressure_data(files)
    correlation, metrics = analyzer.calculate_correlation(pressures)

    print(f"Correlation score: {correlation:.3f}")

    if correlation >= 0.7:
        print("🎉 EXCELLENT - SD card data strongly validates mobile app")
    elif correlation >= 0.4:
        print("✅ GOOD - SD card data confirms mobile app readings")
    else:
        print("⚠️ MODERATE - Use mobile app data for clinical decisions")

    print(f"Pressure difference: {metrics['pressure_diff']:.1f} cmH₂O")

    if metrics['pressure_diff'] <= 1.0:
        print("✅ Optimal pressure validation")
    elif metrics['pressure_diff'] <= 2.0:
        print("⚠️ Acceptable pressure validation")
    else:
        print("❌ Review pressure validation")

if __name__ == "__main__":
    # Run examples (uncomment the ones you want to try)

    example_basic_usage()
    # example_custom_reference_data()
    # example_different_timeframes()
    # example_correlation_interpretation()
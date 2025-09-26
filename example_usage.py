#!/usr/bin/env python3
"""
Example usage of BMC Sleep Study Analyzer
Shows how to perform comprehensive sleep study analysis
"""

from bmc_sleep_analyzer import BMCSleepAnalyzer

def example_basic_usage():
    """Basic usage example - comprehensive analysis"""
    print("=== BASIC COMPREHENSIVE ANALYSIS ===")

    # Create analyzer (auto-detects device ID)
    analyzer = BMCSleepAnalyzer()

    # Run complete sleep study analysis for last 6 months
    analyzer.run_complete_analysis(months=6)

def example_recent_data_focus():
    """Example focusing on recent data"""
    print("\n=== RECENT DATA ANALYSIS ===")

    # Create analyzer
    analyzer = BMCSleepAnalyzer("23804346")

    # Analyze just the last 3 months for recent therapy assessment
    analyzer.run_complete_analysis(months=3)

def example_complete_dataset_analysis():
    """Example analyzing complete dataset"""
    print("\n=== COMPLETE DATASET ANALYSIS ===")

    analyzer = BMCSleepAnalyzer()

    # Analyze complete dataset (all available files)
    print("Analyzing complete dataset for long-term trends...")
    analyzer.run_complete_analysis(months=None)

def example_clinical_insights():
    """Example showing how to interpret clinical results"""
    print("\n=== CLINICAL INTERPRETATION ===")

    analyzer = BMCSleepAnalyzer()

    # Run analysis and get results
    results = analyzer.analyze_comprehensive_data(months=6)

    if results:
        clinical = results.get('clinical_assessment', {})
        pressure_data = results.get('pressure_analysis', {})

        print(f"Therapy Effectiveness: {clinical.get('therapy_effectiveness', 'Unknown')}")
        print(f"Compliance Status: {clinical.get('compliance_status', 'Unknown')}")

        if 'statistics' in pressure_data:
            stats = pressure_data['statistics']
            print(f"Mean Pressure: {stats['mean']:.1f} cmH₂O")
            print(f"Pressure Range: {stats['min']:.1f}-{stats['max']:.1f} cmH₂O")

            # Clinical interpretation
            if stats['mean'] > 15.0:
                print("⚠️ High pressure detected - may indicate therapy optimization needed")
            elif 6.0 <= stats['mean'] <= 12.0:
                print("✅ Pressure in optimal therapeutic range")
            else:
                print("📊 Pressure outside typical range - clinical review recommended")

def example_custom_timeframe():
    """Example with detailed analysis parameters"""
    print("\n=== CUSTOM ANALYSIS ===")

    analyzer = BMCSleepAnalyzer()

    # You can also access individual analysis components
    files = analyzer._get_recent_files(months=3)
    print(f"Found {len(files)} files for analysis")

    pressure_data = analyzer._extract_pressure_data(files)
    print(f"Extracted {pressure_data['total_readings']:,} pressure readings")

    # Perform targeted pressure analysis
    pressure_analysis = analyzer._analyze_pressure_therapy(pressure_data)
    stats = pressure_analysis.get('statistics', {})

    if stats:
        print(f"Mean pressure: {stats['mean']:.1f} cmH₂O")
        print(f"Pressure stability (SD): {stats['std']:.1f}")

        # Custom assessment
        if stats['std'] < 2.0:
            print("✅ Excellent pressure stability")
        elif stats['std'] < 3.0:
            print("✅ Good pressure stability")
        else:
            print("⚠️ Variable pressure - may need titration review")

if __name__ == "__main__":
    # Run examples (uncomment the ones you want to try)

    example_basic_usage()
    # example_recent_data_focus()
    # example_complete_dataset_analysis()
    # example_clinical_insights()
    # example_custom_timeframe()
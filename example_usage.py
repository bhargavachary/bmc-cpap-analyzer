#!/usr/bin/env python3
"""
Example usage of BMC Sleep Study Analyzer
Shows how to perform comprehensive sleep study analysis and detailed event extraction
"""

from bmc_sleep_analyzer import BMCSleepAnalyzer
from detailed_event_analyzer import DetailedEventAnalyzer

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

def example_detailed_event_analysis():
    """NEW: Example of detailed event analysis"""
    print("\n=== DETAILED EVENT ANALYSIS (NEW) ===")

    event_analyzer = DetailedEventAnalyzer()

    # Extract detailed events from recent files
    print("Extracting detailed sleep events...")
    events_data, pressure_data = event_analyzer.extract_detailed_events(recent_files_only=True)

    if events_data:
        # Create comprehensive event charts
        print("Creating detailed event visualizations...")
        event_analyzer.create_detailed_event_charts(events_data, pressure_data)

        # Generate detailed report
        print("Generating detailed event report...")
        detailed_report = event_analyzer.generate_detailed_report(events_data, pressure_data)

        # Print summary
        total_events = sum(len(night['events']) for night in events_data.values())
        total_nights = len(events_data)

        print(f"\n📊 Event Analysis Results:")
        print(f"• Nights analyzed: {total_nights}")
        print(f"• Total events detected: {total_events}")
        print(f"• Average events per night: {total_events/total_nights:.1f}")

        # Show sample events from first night
        first_night = list(events_data.values())[0]
        if first_night['events']:
            print(f"\n🔍 Sample events from Night 1:")
            for i, event in enumerate(first_night['events'][:5], 1):
                print(f"  {i}. {event['timestamp']} - {event['type']} ({event['severity']})")
                if 'pressure_increase' in event:
                    print(f"     Pressure increase: {event['pressure_increase']:.1f} cmH₂O")

        print(f"\n📁 Files generated:")
        print(f"• detailed_sleep_events.png")
        print(f"• detailed_sleep_events_report.txt")
        print(f"• detailed_sleep_events_data.json")

    else:
        print("❌ No event data could be extracted")

def example_combined_analysis():
    """Example combining both analyzers for complete assessment"""
    print("\n=== COMBINED COMPREHENSIVE ANALYSIS ===")

    # Run basic sleep study analysis
    print("1. Running comprehensive sleep study analysis...")
    sleep_analyzer = BMCSleepAnalyzer()
    sleep_results = sleep_analyzer.analyze_comprehensive_data(months=3)

    # Run detailed event analysis
    print("2. Running detailed event extraction...")
    event_analyzer = DetailedEventAnalyzer()
    events_data, pressure_data = event_analyzer.extract_detailed_events()

    if sleep_results and events_data:
        # Compare findings
        pressure_stats = sleep_results.get('pressure_analysis', {}).get('statistics', {})
        total_events = sum(len(night['events']) for night in events_data.values())

        print(f"\n📊 COMBINED INSIGHTS:")
        print(f"• Mean pressure: {pressure_stats.get('mean', 0):.1f} cmH₂O")
        print(f"• Pressure stability: {sleep_results.get('pressure_analysis', {}).get('therapy_assessment', {}).get('pressure_stability', 'Unknown')}")
        print(f"• Events detected: {total_events}")
        print(f"• Therapy effectiveness: {sleep_results.get('clinical_assessment', {}).get('therapy_effectiveness', 'Unknown')}")

        print(f"\n🔬 CLINICAL CORRELATION:")
        if total_events > 150:
            print("• High event activity detected - correlates with pressure variability")
        elif total_events > 50:
            print("• Moderate event activity - CPAP responding appropriately")
        else:
            print("• Low event activity - excellent therapy control")

if __name__ == "__main__":
    # Run examples (uncomment the ones you want to try)

    example_basic_usage()
    # example_recent_data_focus()
    # example_complete_dataset_analysis()
    # example_clinical_insights()
    # example_custom_timeframe()
    # example_detailed_event_analysis()  # NEW!
    # example_combined_analysis()  # NEW!
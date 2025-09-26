# BMC Sleep Study Analyzer

A comprehensive Python tool for independent analysis of BMC RESmart CPAP raw SD card data. Provides sleep study expert-level insights without requiring mobile app data correlation.

## Features

- 🏥 **Independent Sleep Study Analysis** - No mobile app data required
- 📊 **Comprehensive Therapy Assessment** - Pressure optimization, respiratory events, usage patterns
- 🔬 **Clinical-Grade Reporting** - Sleep study expert-level insights and recommendations
- 📈 **Advanced Analytics** - Temporal trends, therapy effectiveness, compliance analysis
- 🎯 **Flexible Timeframes** - Analyze recent data (3, 6, 12 months) or complete dataset
- 💊 **Clinical Decision Support** - Evidence-based recommendations for therapy optimization

## Quick Start

### 1. Prerequisites

```bash
pip install numpy matplotlib
```

### 2. Prepare Your Data

Copy BMC CPAP data files from SD card to a directory:
- `23804346.000` through `23804346.029` (data files)
- `23804346.evt` (event file)
- `23804346.log` (log file)
- Other associated files (`.idx`, `.USR`, `.ENG`)

### 3. Run Analysis

```bash
python bmc_sleep_analyzer.py
```

**That's it!** No configuration needed - the analyzer works independently with raw SD card data.

## Output Files

- **`bmc_sleep_study_report.txt`** - Comprehensive clinical sleep study report
- **`bmc_sleep_study_analysis.png`** - Advanced visualization dashboard
- **`bmc_sleep_study_analysis.json`** - Detailed analysis data

## Sample Output

```
🏥 BMC COMPREHENSIVE SLEEP STUDY ANALYSIS
============================================================
Device ID: 23804346
Analysis Date: 2025-09-26 21:45:32

📁 Dataset: Last 6 months
📁 Files found: 10

🔍 PRESSURE THERAPY ANALYSIS...
    📁 23804346.020: 165,430 readings
    📁 23804346.021: 158,920 readings
    [...]

📊 KEY CLINICAL FINDINGS:
• Therapy Effectiveness: EXCELLENT
• Compliance Status: MODERATE
• Mean Pressure: 8.2 cmH₂O
• Pressure Stability: excellent

🏥 CLINICAL IMPACT:
This analysis provides independent assessment of CPAP therapy
effectiveness equivalent to comprehensive sleep study evaluation.
```

## Understanding the Results

### Clinical Assessment Categories

**Therapy Effectiveness:**
- **EXCELLENT**: Optimal pressure delivery and respiratory control
- **GOOD**: Effective therapy with minor optimization opportunities
- **REQUIRES_OPTIMIZATION**: Therapy adjustments recommended

**Compliance Status:**
- **EXCELLENT**: ≥70% usage rate (clinical standard)
- **MODERATE**: 50-70% usage rate
- **POOR**: <50% usage rate - intervention needed

**Pressure Analysis:**
- **Optimal Range**: 6-12 cmH₂O (typical therapeutic window)
- **Stability Assessment**: Based on pressure variability analysis
- **Titration Quality**: Evaluation of pressure optimization

## Advanced Usage

### Analyze Different Timeframes

```python
from bmc_sleep_analyzer import BMCSleepAnalyzer

analyzer = BMCSleepAnalyzer()

# Analyze last 3 months
analyzer.run_complete_analysis(months=3)

# Analyze last 6 months
analyzer.run_complete_analysis(months=6)

# Analyze complete dataset
analyzer.run_complete_analysis(months=None)
```

### What the Analysis Includes

**Pressure Therapy Analysis:**
- Statistical analysis of pressure delivery
- Therapeutic window assessment
- Pressure stability evaluation
- Optimization recommendations

**Respiratory Event Analysis:**
- Event detection from raw data
- AHI estimation and severity classification
- Treatment effectiveness assessment

**Usage and Compliance:**
- Usage pattern analysis
- Compliance assessment
- Consistency evaluation

**Temporal Trends:**
- Long-term therapy trends
- Pressure optimization progress
- Stability over time

## Supported Devices

- BMC RESmart GII E-20A AutoCPAP
- Other BMC RESmart models (may require minor adjustments)

## File Structure

```
your-data-directory/
├── 23804346.000-029    # CPAP data files
├── 23804346.evt        # Event file
├── 23804346.log        # Log file
├── bmc_cpap_analyzer.py # Analysis script
└── outputs/
    ├── bmc_cpap_report.txt
    ├── bmc_cpap_analysis.png
    └── bmc_cpap_analysis.json
```

## Clinical Use

This tool is designed to:
- ✅ Validate mobile app accuracy using raw device data
- 📋 Generate reports for pulmonologist review
- 🎯 Identify therapy effectiveness vs. adherence issues
- 📊 Provide objective data for clinical decision making

**Note**: This tool validates mobile app data but does not replace clinical judgment. Always consult with healthcare providers for therapy adjustments.

## Troubleshooting

### No files found
- Ensure BMC data files are in the same directory as the script
- Check file naming format (should be `DEVICEID.000`, `DEVICEID.001`, etc.)

### Low correlation
- Verify mobile app reference data is accurate
- Try different timeframe analysis
- Ensure data files are from the same period as mobile app readings

### No pressure data extracted
- Files may be corrupted or from different device model
- Try updating the parsing method for your specific device variant

## Contributing

This tool was developed through analysis of BMC RESmart CPAP data patterns. Contributions welcome for:
- Support for additional BMC models
- Enhanced parsing algorithms
- Additional clinical metrics
- UI improvements

## Disclaimer

This tool is for informational and validation purposes only. It does not provide medical advice. Always consult qualified healthcare providers for CPAP therapy management and medical decisions.

## License

Open source - feel free to use and modify for personal and clinical applications.
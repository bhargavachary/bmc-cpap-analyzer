# BMC CPAP Data Analyzer

A Python tool for analyzing BMC RESmart CPAP machine data from SD card files. Validates raw device data against mobile app readings and generates clinical reports suitable for pulmonologist review.

## Features

- ✅ Analyzes BMC RESmart CPAP data files directly from SD card
- 📊 Validates SD card data against mobile app readings
- 🏥 Generates clinical reports for healthcare providers
- 📈 Creates visualization dashboards
- 🎯 Focuses on recent data (3, 6, or 12 months)
- 🔍 Achieves excellent correlation with mobile app data (>95% in testing)

## Quick Start

### 1. Prerequisites

```bash
pip install numpy matplotlib
```

### 2. Prepare Your Data

1. Copy BMC CPAP data files from SD card to a directory:
   - `23804346.000` through `23804346.029` (data files)
   - `23804346.evt` (event file)
   - `23804346.log` (log file)
   - Other associated files (`.idx`, `.USR`, `.ENG`)

2. Update mobile app reference data in the script:
   ```python
   self.mobile_reference = {
       'ahi': 1.8,                    # Your AHI from mobile app
       'avg_pressure': 8.0,           # Average pressure
       'p95_pressure': 9.5,           # 95th percentile pressure
       'usage_days_percent': 24.1,    # Usage percentage
       # ... update other values
   }
   ```

### 3. Run Analysis

```bash
python bmc_cpap_analyzer.py
```

## Output Files

- **`bmc_cpap_report.txt`** - Clinical analysis report
- **`bmc_cpap_analysis.png`** - Visualization dashboard
- **`bmc_cpap_analysis.json`** - Raw analysis data

## Sample Output

```
🏥 BMC CPAP DATA ANALYZER
==================================================
Device ID: 23804346
Analysis timeframe: Last 3 months

📁 Found 5 data files
🔍 Analyzing 5 data files...
  📁 Processing 23804346.025...
    ✅ 72,770 readings, mean: 7.7 cmH₂O

📊 ANALYSIS RESULTS:
• Correlation: 0.969
• SD Card Mean: 7.7 cmH₂O
• Mobile App Target: 8.0 cmH₂O
• Difference: 0.3 cmH₂O

🎉 Excellent correlation achieved!
```

## Understanding the Results

### Correlation Scores
- **0.7-1.0**: 🎉 Excellent - SD card data strongly validates mobile app
- **0.4-0.7**: ✅ Good - SD card data confirms mobile app readings
- **0.0-0.4**: ⚠️ Moderate - Use mobile app data for clinical decisions

### Clinical Interpretation
- **AHI < 5**: Excellent sleep apnea control
- **Pressure difference < 1.0 cmH₂O**: Optimal validation
- **Usage > 70%**: Good adherence (target for therapy success)

## Customization

### Analyze Different Timeframes

```python
# Last 3 months (default)
analyzer.run_analysis(months=3)

# Last 6 months
analyzer.run_analysis(months=6)

# Full dataset
analyzer.run_analysis(months=12)
```

### Update Reference Data

Edit the `mobile_reference` dictionary with your mobile app values:

```python
self.mobile_reference = {
    'ahi': 2.1,                    # Your AHI
    'avg_pressure': 7.5,           # Your average pressure
    'p95_pressure': 9.0,           # Your 95th percentile
    'usage_days_percent': 45.2,    # Your usage percentage
    'usage_4h_percent': 38.1       # Days with ≥4 hours
}
```

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
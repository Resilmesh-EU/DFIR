# DFIR Report Generation System

This example demonstrates how to create a sequential workflow using two CAI agents with professional HTML report templating:

1. **DFIR Agent**: Performs digital forensics and incident response analysis
2. **Reporting Agent**: Generates professional HTML reports using structured templates

## ✨ New Features (Latest Update)

- **🌍 English Interface**: All prompting and interface in English
- **🎯 Default DFIR Prompt**: Intelligent default prompt for Wazuh log analysis
- **🎨 Professional HTML Template**: Modern CSS with placeholder system
- **📊 Visual Timeline**: Interactive attack progression timeline
- **🏷️ MITRE ATT&CK Tagging**: Automatic technique identification
- **📈 Statistics Cards**: Animated metric visualizations
- **🔍 IOC Extraction**: Structured indicators of compromise
- **⚡ Template Placeholder System**: 12 structured content placeholders

## Files Structure

```
dfir_report/
├── __init__.py                 # Package initialization
├── main.py                     # Main orchestrator (English interface)
├── html_report_template.html   # Professional HTML template ✨ NEW
├── agents/
│   ├── __init__.py             # Agents package init
│   ├── dfir_agent.py           # DFIR analysis agent
│   └── reporting_agent.py      # HTML report generation agent (updated)
├── test_data/
│   └── corvega_log.json        # Sample Wazuh log for testing
├── dfir_reports/               # Generated reports directory
├── .env                        # Environment variables
├── README.md                   # This file
└── example_usage.py            # Usage examples
```

## Installation

1. **Set up CAI framework in virtual environment:**
```bash
# Create and activate virtual environment
python3 -m venv cai_venv
source cai_venv/bin/activate  # On Windows: cai_venv\Scripts\activate

# Install CAI framework in editable mode (from CAI project root)
cd /path/to/cai/project/root
pip install -e .
```

2. **Configure environment variables in `.env`:**
```bash
# Required
OPENAI_API_KEY="your-openai-api-key"
CAI_MODEL="gpt-4o"

# Optional (for enhanced capabilities)
PERPLEXITY_API_KEY="your-perplexity-key"  # Web search
SHODAN_API_KEY="your-shodan-key"          # IP intelligence
GOOGLE_SEARCH_API_KEY="your-google-key"   # Google search
GOOGLE_SEARCH_CX="your-search-cx"         # Custom search
```

## Usage

### Interactive Mode (English Interface)

```bash
# Make sure virtual environment is activated
source cai_venv/bin/activate

# Navigate to dfir_report directory
cd examples/dfir_report

# Run interactive mode
python main.py
```

**Interactive prompts:**
- **📝 DFIR analysis prompt**: Press Enter for **default Wazuh analysis prompt**
- **📁 File path**: Path to analyze (optional)
- **📋 Incident title**: Report title (optional)

### 🎯 Default DFIR Prompt

When you press Enter without providing a prompt, the system automatically generates:
```
"Using the Wazuh log in {file_path} please conduct a complete forensics analysis to discover the potential entry points of the attacker, pivoting points, and objectives"
```

### Programmatic Usage

```python
import asyncio
from main import DFIRReportManager

async def run_analysis():
    manager = DFIRReportManager()
    
    # Use default prompt (user_prompt=None)
    dfir_analysis, html_report = await manager.run_complete_workflow(
        user_prompt=None,  # Uses intelligent default prompt
        file_path="test_data/corvega_log.json",
        incident_title="Wazuh ICS Security Incident"
    )
    
    print("✅ Analysis completed!")
    print(f"📊 DFIR Analysis: {len(dfir_analysis)} characters")
    print(f"📄 HTML Report: {len(html_report)} characters")

# Run the analysis
asyncio.run(run_analysis())
```

## 🎨 HTML Report Template System

### Template Features

The system uses a professional HTML template (`html_report_template.html`) with:

- **🎨 Modern CSS Design**: Gradients, shadows, animations, responsive layout
- **📱 Responsive Layout**: Works on desktop, tablet, and mobile
- **🔧 Placeholder System**: 12 structured placeholders for content
- **⏱️ Visual Timeline**: Interactive timeline with dots and cards
- **📊 Statistics Cards**: Animated metric cards with hover effects
- **🌐 IP Address Cards**: Color-coded (primary, external, default)
- **🏷️ MITRE ATT&CK Tags**: Professional technique tagging
- **🔍 IOC Organization**: Structured indicators of compromise
- **💡 Recommendation Boxes**: Immediate and long-term actions

### Template Placeholders

| Placeholder | Description |
|-------------|-------------|
| `{{INCIDENT_TITLE}}` | Main incident title |
| `{{INCIDENT_DATES}}` | Incident and analysis dates |
| `{{EXECUTIVE_SUMMARY}}` | Management-friendly overview |
| `{{STATISTICS_CARDS}}` | Attack metrics and statistics |
| `{{ENTRY_POINTS_CONTENT}}` | Compromised systems and entry points |
| `{{TIMELINE_DESCRIPTION}}` | Timeline overview |
| `{{TIMELINE_EVENTS}}` | Detailed chronological events |
| `{{ATTACK_OBJECTIVES}}` | Categorized attacker goals |
| `{{IOCS_CONTENT}}` | All indicators of compromise |
| `{{RECOMMENDATIONS_CONTENT}}` | Security recommendations |
| `{{FORENSIC_CONCLUSION}}` | Professional conclusion |
| `{{REPORT_FOOTER}}` | Attribution and classification |

### CSS Classes Available

```css
.stat-card              /* Statistics cards */
.ip-card                /* IP address cards */
.ip-card.primary        /* Primary attack IP */
.ip-card.external       /* External C2 servers */
.timeline-item          /* Timeline events */
.timeline-content       /* Event content */
.timeline-time          /* Event timestamps */
.timeline-dot           /* Timeline visual dots */
.objective-card         /* Attack objectives */
.recommendation-box     /* Recommendations */
.mitre-tag              /* MITRE ATT&CK techniques */
.alert-critical         /* Critical security alerts */
.ioc-list               /* IOC listings */
```

## Testing

### Quick Test with Sample Data

```bash
# Activate environment and navigate
source cai_venv/bin/activate
cd examples/dfir_report

# Run with sample data
python main.py
```

**When prompted:**
- **Prompt**: Press `Enter` for default
- **File**: `test_data/corvega_log.json`
- **Title**: `Wazuh ICS Security Incident`

### Expected Output

The system will:
1. **Generate default prompt**: `"Using the Wazuh log in test_data/corvega_log.json please conduct a complete forensics analysis..."`
2. **Run DFIR analysis**: Extract timeline, IOCs, MITRE techniques
3. **Generate professional HTML report** with:
   - Executive summary
   - Statistics cards (duration, alerts, IPs, techniques)
   - Visual timeline of attack progression
   - Entry points analysis
   - Attack objectives categorization
   - IOCs extraction (IPs, domains, files)
   - Security recommendations

## Example Output Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Wazuh ICS Security Incident - Forensic Analysis Report</title>
    <!-- Modern CSS with gradients, animations, responsive design -->
</head>
<body>
    <div class="container">
        <!-- Professional header with gradient background -->
        <div class="header">
            <h1>COMPREHENSIVE FORENSIC ANALYSIS REPORT</h1>
            <p class="subtitle">Wazuh ICS Security Incident</p>
        </div>
        
        <!-- Executive summary for management -->
        <div class="executive-summary">...</div>
        
        <!-- Animated statistics cards -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="number">19s</div>
                <div class="label">Attack Duration</div>
            </div>
            <!-- More stat cards... -->
        </div>
        
        <!-- Visual timeline with interactive elements -->
        <div class="timeline">...</div>
        
        <!-- Color-coded IOCs and recommendations -->
        <!-- ... -->
    </div>
</body>
</html>
```

## Troubleshooting

### Common Issues

1. **❌ Import Errors**: Ensure CAI framework is installed
   ```bash
   source cai_venv/bin/activate
   pip install -e .  # From CAI project root
   ```

2. **❌ Template Not Found**: Verify `html_report_template.html` exists
   ```bash
   ls examples/dfir_report/html_report_template.html
   ```

3. **❌ API Authentication**: Check `.env` file has valid `OPENAI_API_KEY`
   ```bash
   cat examples/dfir_report/.env | grep OPENAI_API_KEY
   ```

4. **❌ File Path Issues**: Use absolute paths or verify file existence
   ```bash
   ls examples/dfir_report/test_data/corvega_log.json
   ```

### Verification Checklist

- ✅ Virtual environment activated
- ✅ CAI framework installed (`pip install -e .`)
- ✅ Environment variables configured
- ✅ HTML template file exists
- ✅ Test data file exists
- ✅ Output directory writable

## Integration with CAI

This example demonstrates:

- **🔧 Agent Composition**: Specialized agents with custom templates
- **🔄 Sequential Workflows**: Chaining agents for complex tasks
- **🛠️ Tool Integration**: CAI's built-in security tools
- **📄 Template-Based Reporting**: Professional document generation
- **🎯 Smart Prompting**: Default prompts with intelligent fallbacks
- **🔄 Output Processing**: Structured template placeholder replacement
- **🌍 Professional Interface**: English prompting system

### Key Innovations

- **🧠 Default Prompt System**: Intelligent prompt generation for Wazuh logs
- **🎨 HTML Template Engine**: Professional report formatting with CSS
- **🔧 Placeholder Architecture**: Structured content replacement
- **🏷️ MITRE ATT&CK Integration**: Automatic technique tagging
- **⏱️ Visual Timeline Generation**: Interactive attack progression
- **🔍 IOC Extraction**: Automatic indicator identification and formatting

## Customization & Extension

### 1. **Customize Template**
Edit `html_report_template.html` for your organization's branding:
```html
<!-- Change colors, logos, styling -->
.header {
    background: linear-gradient(135deg, #your-color1, #your-color2);
}
```

### 2. **Add New Placeholders**
Extend the template system:
```python
# In main.py, add new placeholder
report_prompt += f"{{{{NEW_SECTION}}}}: Your custom content here"
```

### 3. **Custom Default Prompts**
Create domain-specific prompts:
```python
# In dfir_agent.py
if "azure" in file_path.lower():
    default_prompt = "Analyze this Azure log for cloud security threats..."
elif "aws" in file_path.lower():
    default_prompt = "Examine this AWS CloudTrail for suspicious activity..."
```

### 4. **Additional Output Formats**
Extend to PDF, Word, or other formats:
```python
# Add to reporting_agent.py
@function_tool
def generate_pdf_report(html_content: str) -> str:
    # Convert HTML to PDF
    pass
```

## Next Steps

1. **🎨 Customize Template**: Modify `html_report_template.html` for your branding
2. **🔧 Extend Placeholders**: Add new template sections and placeholders
3. **🛠️ Add Tools**: Integrate additional CAI tools for enhanced analysis
4. **🎯 Custom Prompts**: Create domain-specific default prompts
5. **📄 Report Formats**: Extend to PDF, Word, or other output formats
6. **🔗 Integrations**: Connect with SIEM systems, ticketing platforms
7. **📊 Analytics**: Add report analytics and metrics

## Contributing

To contribute to this example:
1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Test with sample data
5. Submit a pull request

For more advanced usage and customization options, refer to the individual agent files and the main CAI documentation.

---

**🎉 Ready to generate professional DFIR reports with CAI!**
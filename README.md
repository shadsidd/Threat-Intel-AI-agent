# Threat Intelligence Aggregator

A cybersecurity threat intelligence tool built with Agno that automatically aggregates and summarizes recent threat data from multiple sources.

## Overview

This tool uses specialized AI agents to collect threat intelligence from:
- Web searches for recent cybersecurity threat reports
- X (Twitter) analysis for mentions of emerging threats
- Official vulnerability feeds (NVD and US-CERT)

The collected data is combined into a comprehensive threat intelligence report with sections covering threat actors, targeted industries, attack vectors, and TTPs (Tactics, Techniques, and Procedures).

## Features

- **Multi-source intelligence gathering**: Collects data from web searches, social media, and official feeds
- **Automated analysis**: AI-powered summarization and categorization
- **Persistent storage**: Maintains session history in PostgreSQL or SQLite
- **Markdown formatting**: Clean, readable reports
- **Customizable focus**: Can be configured to focus on specific threat groups or broad overviews
- **Interactive UI**: A Streamlit-based user interface for easier configuration and visualization

## Requirements

- Python 3.8+
- PostgreSQL database or SQLite (UI version supports both)
- Agno framework and its dependencies (see requirements.txt)
- Streamlit (for the UI version)

## Setup

1. Install required packages:
   ```
   pip install -r requirements.txt
   ```

2. Set up database:
   - For PostgreSQL:
     - Install PostgreSQL if not already installed
     - Create a database named 'agno'
     - The script uses your system username with no password for local development
   - For SQLite (UI version only):
     - No setup required, just specify a path for the database file

3. Configure the script (optional):
   - Update database credentials if needed
   - Modify RSS feeds in the FEEDS dictionary
   - Adjust agent instructions for different focus areas

## Usage

### Command Line Version

Run the script to generate a threat intelligence report:

```
python threat-intel.py
```

The script will execute the agents, collect intelligence, and output a formatted report.

### Interactive UI Version

Run the Streamlit app for an interactive experience:

```
streamlit run threat-intel-2.py
```

The Streamlit UI provides:
- Model selection dropdown
- API key input
- Database configuration options (PostgreSQL or SQLite)
- Custom search queries
- Option to focus on specific threat actors
- Tabbed interface for viewing results

## Customization

You can customize the threat intelligence focus by modifying the final prompt to the summary agent. For example:

```python
# For a general threat report
response = summary_agent.print_response(
    "Provide a threat intelligence report on recent cybersecurity threats",
    stream=False
)

# For a focused report on a specific threat actor
response = summary_agent.print_response(
    "Provide a threat intelligence report on recent cybersecurity threats, focusing on the Clop ransomware group.",
    stream=False
)
```

## Troubleshooting

### Architecture Issues
If you encounter PostgreSQL architecture compatibility issues on Apple Silicon Macs, use the UI version and select SQLite as the storage option.

### Package Installation
If you get import errors related to `exa_py`, make sure to install it with:
```
pip install exa_py
```

## License

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   Copyright 2024 Shadab Siddiqui

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

This project is licensed under the Apache License 2.0.
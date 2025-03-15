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
- EXA API key (for web search capabilities)

## API Keys Setup

### EXA API Key
The tool uses EXA (a powerful search engine API that provides comprehensive web search capability) for web searches and threat intelligence gathering. You need to obtain an API key:

1. Sign up for an API key at [EXA's website](https://exa.ai)
2. Set up the API key in one of the following ways:
   - Set as an environment variable:
     ```bash
     export EXA_API_KEY=your_api_key_here
     ```
   - For the UI version, enter the API key directly in the Streamlit interface
   
Without a valid EXA API key, the web search functionality will not work, limiting the tool's ability to gather real-time threat intelligence.

### Gemini API Key
For the LLM functionality:
1. Obtain a Gemini API key from [Google AI Studio](https://ai.google.dev/)
2. Provide it when using the tool (UI version) or set it in your environment

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

### API Key Issues
If you see search-related errors, verify that:
- Your EXA API key is correctly set in the environment or UI
- The API key is valid and has sufficient quota remaining

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
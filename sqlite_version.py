from agno.agent import Agent
from agno.models.google import Gemini  # Gemini as LLM
from agno.tools.exa import ExaTools
from agno.storage.agent.sqlite import SQLiteAgentStorage  # Using SQLite instead of PostgreSQL
from datetime import datetime
import os
import getpass

# Define RSS feeds
FEEDS = {
    "nvd": "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml",
    "us_cert": "https://www.cisa.gov/uscert/ncas/alerts.xml",
}

# Database setup for session persistence using SQLite
storage = SQLiteAgentStorage(
    table_name="threat_intel_sessions",
    db_url="sqlite:///threat_intel.db"  # Local SQLite file
)

# Agent 1: Web Search Agent
web_agent = Agent(
    name="WebSearchAgent",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[ExaTools()],
    instructions=[
        "Search the web for cybersecurity threat reports from the last 7 days.",
        "Include a variety of threats (e.g., ransomware, phishing, vulnerabilities), not just one group.",
        "Return findings in concise markdown format with URLs."
    ],
    show_tool_calls=False,  # Hide tool execution details in output
    markdown=True
)

# Agent 2: X Analysis Agent
x_agent = Agent(
    name="XAnalysisAgent",
    model=Gemini(id="gemini-2.0-flash"),
    instructions=[
        "Analyze recent X posts for mentions of cybersecurity threats.",
        "Cover a range of threats, not limited to a single group.",
        "Return findings in concise markdown format with timestamps and usernames."
    ],
    show_tool_calls=False,  # Clean output
    markdown=True
)

# Agent 3: Feed Reader Agent
feed_agent = Agent(
    name="FeedReaderAgent",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[ExaTools()],  # Fallback to search if direct fetch isn't supported
    instructions=[
        "Search for recent cybersecurity updates from NVD (nvd.nist.gov) and US-CERT (cisa.gov).",
        f"Alternatively, if you can fetch directly, retrieve content from: {', '.join(FEEDS.values())}.",
        "Summarize key vulnerabilities or alerts in concise markdown format.",
        "Include source (NVD or US-CERT) and titles of updates."
    ],
    show_tool_calls=False,
    markdown=True
)

# Agent 4: Summary Agent (Team Leader)
summary_agent = Agent(
    name="SummaryAgent",
    model=Gemini(id="gemini-2.0-flash"),
    team=[web_agent, x_agent, feed_agent],
    storage=storage,
    instructions=[
        "Combine findings from WebSearchAgent, XAnalysisAgent, and FeedReaderAgent into a single report.",
        "Format the report in markdown with the following structure:",
        "- Header: 'Threat Intelligence Report'",
        "- Timestamp: Current date and time",
        "- Sections: 'Summary', 'Threat Actors', 'Targeted Industries', 'Attack Vectors', 'TTPs', 'Feed Updates'",
        "Include a variety of recent cybersecurity threats in all sections.",
        "Ensure the output is clean and readable."
    ],
    show_tool_calls=False,
    markdown=True,
    add_history_to_messages=True
)

# Execute and print the response cleanly
if __name__ == "__main__":
    print("Generating threat intelligence report using SQLite storage...")
    response = summary_agent.print_response(
        "Provide a threat intelligence report on recent cybersecurity threats",
        stream=False  # Non-streaming for a complete, polished output
    )
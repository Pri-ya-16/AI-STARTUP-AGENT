from google.adk.agents import LlmAgent
from google.adk.tools import google_search

root_agent = LlmAgent(
    name="market_research_agent",
    model="gemini-pro",
    description="Market research assistant",
    instruction="Provide market insights using Google Search.",
    tools=[google_search]
)
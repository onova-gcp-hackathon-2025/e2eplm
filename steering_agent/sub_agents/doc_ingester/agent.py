"""
DocIngester agent for ingesting and extracting requirements from IBM DOORS exports and PDF response documents.
"""

from google.adk import Agent
from ...prompt import DOC_INGESTER_PROMPT
from ...model import MODEL
from steering_agent.tools.ibm_doors_fetcher import fetch_requirements_from_ibm_doors

doc_ingester_agent = Agent(
    model=MODEL,
    name="doc_ingester_agent",
    instruction=DOC_INGESTER_PROMPT,
    output_key="extracted_requirements_output",
    tools=[fetch_requirements_from_ibm_doors],
)

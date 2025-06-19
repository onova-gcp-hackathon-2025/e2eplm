from google.adk import Agent
from ...prompt import DOORS_CONNECTOR_PROMPT
from ...model import MODEL
from steering_agent.tools.ibm_doors_fetcher import fetch_requirements_from_ibm_doors

doors_connector_agent = Agent(
    model=MODEL,
    name="doors_connector_agent",
    instruction=DOORS_CONNECTOR_PROMPT,
    output_key="doors_requirements_output",
    tools=[fetch_requirements_from_ibm_doors],
)

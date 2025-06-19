from google.adk import Agent
from ...prompt import REQUIREMENTS_CURATOR_PROMPT
from ...model import MODEL
from steering_agent.tools.ibm_doors_fetcher import fetch_requirements_from_ibm_doors

requirements_curator_agent = Agent(
    model=MODEL,
    name="requirements_curator_agent",
    instruction=REQUIREMENTS_CURATOR_PROMPT,
    output_key="curated_requirements_output",
    tools=[fetch_requirements_from_ibm_doors],
)

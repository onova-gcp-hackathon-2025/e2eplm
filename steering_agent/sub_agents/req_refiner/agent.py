"""
ReqRefiner agent for reviewing and improving requirements quality.
"""

from google.adk import Agent
from ...prompt import REQ_REFINER_PROMPT
from ...model import MODEL

req_refiner_agent = Agent(
    model=MODEL,
    name="req_refiner_agent",
    instruction=REQ_REFINER_PROMPT,
    output_key="refined_requirements_output",
    tools=[],  # Add tools if needed
)

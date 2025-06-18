"""
ReportGenerator agent for generating validation reports and maintaining traceability.
"""

from google.adk import Agent
from ...prompt import REPORT_GENERATOR_PROMPT
from ...model import MODEL

report_generator_agent = Agent(
    model=MODEL,
    name="report_generator_agent",
    instruction=REPORT_GENERATOR_PROMPT,
    output_key="report_output",
    tools=[],  # Add tools if needed
)

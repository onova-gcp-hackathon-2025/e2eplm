"""
ReqPilot Steering Agent: Orchestrates requirements validation for aerospace engineering.
"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .model import MODEL
from .prompt import REQPILOT_PROMPT
from .sub_agents.req_refiner import req_refiner_agent

# doc_ingester_agent = agent_manager.get_agent("doc_ingester")
# gap_analyzer_agent = agent_manager.get_agent("gap_analyzer")
# report_generator_agent = agent_manager.get_agent("report_generator")

# Define the LlmAgent as the root agent
root_agent = LlmAgent(
    name="steering_agent",
    model=MODEL,
    description=(
        "Coordinates requirements ingestion, refinement, gap analysis, and reporting for aerospace engineering. "
        "Orchestrates sub-agents to validate requirements coverage and generate actionable reports."
    ),
    instruction=REQPILOT_PROMPT,
    output_key="validation_report",
    tools=[
        AgentTool(agent=req_refiner_agent),
        # AgentTool(agent=doc_ingester_agent),
        # AgentTool(agent=gap_analyzer_agent),
        # AgentTool(agent=report_generator_agent),
    ],
)

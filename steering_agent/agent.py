"""
ReqPilot Steering Agent: Orchestrates requirements validation for aerospace engineering.
"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .model import MODEL
from .prompt import REQPILOT_PROMPT
from .sub_agents.req_refiner import req_refiner_agent
from .sub_agents.gap_analyzer import gap_analyzer_agent
from .sub_agents.doc_ingester import doc_ingester_agent
from steering_agent.tools.ibm_doors_fetcher import fetch_requirements_from_ibm_doors

# report_generator_agent = agent_manager.get_agent("report_generator")

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
        AgentTool(agent=doc_ingester_agent),
        AgentTool(agent=req_refiner_agent),
        AgentTool(agent=gap_analyzer_agent),
        # AgentTool(agent=report_generator_agent),
        fetch_requirements_from_ibm_doors
    ],
)

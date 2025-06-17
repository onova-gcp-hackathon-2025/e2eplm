"""
GapAnalyzer Agent
Evaluates coverage and alignment between source requirements and engineering response documents.
"""

from google.adk import Agent
from ...prompt import GAP_ANALYZER_PROMPT
from ...model import MODEL

gap_analyzer_agent = Agent(
    model=MODEL,
    name="gap_analyzer_agent",
    instruction=GAP_ANALYZER_PROMPT,
    output_key="gap_analysis_output",
)

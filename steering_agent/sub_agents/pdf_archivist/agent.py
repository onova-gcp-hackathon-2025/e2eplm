from google.adk import Agent
from ...prompt import PDF_ARCHIVIST_PROMPT
from ...model import MODEL
from steering_agent.tools.vertexai_search_tool import vertexai_search_tool

pdf_archivist_agent = Agent(
    model=MODEL,
    name="pdf_archivist_agent",
    instruction=PDF_ARCHIVIST_PROMPT,
    output_key="extracted_pdf_requirements_output",
    tools=[vertexai_search_tool],
)

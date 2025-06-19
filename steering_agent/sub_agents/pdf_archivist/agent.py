from google.adk import Agent
from ...prompt import PDF_ARCHIVIST_PROMPT
from ...model import MODEL
from google.adk.tools import VertexAiSearchTool

vertexai_search_tool = VertexAiSearchTool(
   data_store_id="projects/hacker2025-team-12-dev/locations/global/collections/default_collection/dataStores/airquire-reqpilot-requirements-datastore_1750080361972"
)

pdf_archivist_agent = Agent(
    model=MODEL,
    name="pdf_archivist_agent",
    instruction=PDF_ARCHIVIST_PROMPT,
    output_key="extracted_pdf_requirements_output",
    tools=[vertexai_search_tool],
)

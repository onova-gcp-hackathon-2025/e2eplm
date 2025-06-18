import textwrap
import dotenv
import pytest

from steering_agent.sub_agents.req_refiner import req_refiner_agent
from steering_agent.sub_agents.gap_analyzer import gap_analyzer_agent
from steering_agent.sub_agents.doc_ingester import doc_ingester_agent
from steering_agent.sub_agents.report_generator import report_generator_agent
from steering_agent.agent import root_agent

from google.adk.runners import InMemoryRunner
from google.genai.types import Part, UserContent

pytest_plugins = ("pytest_asyncio",)

@pytest.fixture(scope="session", autouse=True)
def load_env():
    dotenv.load_dotenv()

@pytest.mark.asyncio
async def test_req_refiner_agent():
    user_input = textwrap.dedent(
        """
        Requirement: Whenever a test will be performed by the maintenance staff the possibility of maintenance induced faults shall not be allowed.
        Does this requirement make sense?
        """
    ).strip()
    runner = InMemoryRunner(agent=req_refiner_agent)
    session = await runner.session_service.create_session(
        app_name=runner.app_name, user_id="test_user"
    )
    content = UserContent(parts=[Part(text=user_input)])
    response = ""
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content,
    ):
        if event.content.parts and event.content.parts[0].text:
            response = event.content.parts[0].text
    assert "refined" in response.lower() or "revised" in response.lower() or "risk" in response.lower()

@pytest.mark.asyncio
async def test_gap_analyzer_agent():
    user_input = textwrap.dedent(
        """
        Requirement: The system shall implement fault detection and isolation mechanisms in accordance with ARP4754A.
        Response Document: The system includes basic fault detection.
        """
    ).strip()
    runner = InMemoryRunner(agent=gap_analyzer_agent)
    session = await runner.session_service.create_session(
        app_name=runner.app_name, user_id="test_user"
    )
    content = UserContent(parts=[Part(text=user_input)])
    response = ""
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content,
    ):
        if event.content.parts and event.content.parts[0].text:
            response = event.content.parts[0].text
    assert "partially" in response.lower() or "gap" in response.lower()

@pytest.mark.asyncio
async def test_doc_ingester_agent():
    user_input = textwrap.dedent(
        """
        Please ingest the following IBM DOORS requirement export and extract all requirements.
        """
    ).strip()
    runner = InMemoryRunner(agent=doc_ingester_agent)
    session = await runner.session_service.create_session(
        app_name=runner.app_name, user_id="test_user"
    )
    content = UserContent(parts=[Part(text=user_input)])
    response = ""
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content,
    ):
        if event.content.parts and event.content.parts[0].text:
            response = event.content.parts[0].text
    assert "requirement" in response.lower()

@pytest.mark.asyncio
async def test_report_generator_agent():
    user_input = textwrap.dedent(
        """
        Generate a validation summary report for the following requirements and responses.
        """
    ).strip()
    runner = InMemoryRunner(agent=report_generator_agent)
    session = await runner.session_service.create_session(
        app_name=runner.app_name, user_id="test_user"
    )
    content = UserContent(parts=[Part(text=user_input)])
    response = ""
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content,
    ):
        if event.content.parts and event.content.parts[0].text:
            response = event.content.parts[0].text
    assert "report" in response.lower() or "summary" in response.lower()

@pytest.mark.asyncio
async def test_root_agent():
    user_input = textwrap.dedent(
        """
        Please validate the requirements and generate a summary report.
        """
    ).strip()
    runner = InMemoryRunner(agent=root_agent)
    session = await runner.session_service.create_session(
        app_name=runner.app_name, user_id="test_user"
    )
    content = UserContent(parts=[Part(text=user_input)])
    response = ""
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content,
    ):
        if event.content.parts and event.content.parts[0].text:
            response = event.content.parts[0].text
    assert "validation" in response.lower() or "report" in response.lower()

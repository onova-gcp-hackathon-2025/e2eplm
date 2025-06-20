"""Test deployment of Academic Research Agent to Agent Engine."""

import os
import asyncio
from google.adk.sessions import InMemorySessionService, VertexAiSessionService
from vertexai.preview.reasoning_engines import AdkApp
import vertexai
from absl import app, flags
from dotenv import load_dotenv
from vertexai import agent_engines

FLAGS = flags.FLAGS

flags.DEFINE_string("project_id", None, "GCP project ID.")
flags.DEFINE_string("location", None, "GCP location.")
flags.DEFINE_string("bucket", None, "GCP bucket.")
flags.DEFINE_string(
    "resource_id",
    None,
    "ReasoningEngine resource ID (returned after deploying the agent)",
)
flags.DEFINE_string("user_id", None, "User ID (can be any string).")
flags.mark_flag_as_required("resource_id")
flags.mark_flag_as_required("user_id")

def session_service_builder():
  return VertexAiSessionService(location=FLAGS.location, project=FLAGS.project_id)
  # return InMemorySessionService()

def main(argv: list[str]) -> None:  # pylint: disable=unused-argument

    load_dotenv()

    project_id = (
        FLAGS.project_id
        if FLAGS.project_id
        else os.getenv("GOOGLE_CLOUD_PROJECT")
    )
    location = (
        FLAGS.location if FLAGS.location else os.getenv("GOOGLE_CLOUD_LOCATION")
    )
    bucket = (
        FLAGS.bucket
        if FLAGS.bucket
        else os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")
    )

    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION")
    bucket = os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")

    if not project_id:
        print("Missing required environment variable: GOOGLE_CLOUD_PROJECT")
        return
    elif not location:
        print("Missing required environment variable: GOOGLE_CLOUD_LOCATION")
        return
    elif not bucket:
        print(
            "Missing required environment variable: GOOGLE_CLOUD_STORAGE_BUCKET"
        )
        return

    vertexai.init(
        project=project_id,
        location=location,
        staging_bucket=f"gs://{bucket}",
    )

    agent = agent_engines.get(FLAGS.resource_id)
    print(f"Found agent with resource ID: {FLAGS.resource_id} - agent.name: {agent.name}")
    # print(agent.operation_schemas())

    app = AdkApp(
        agent=agent,                                      # Required.
        # app_name="steering_agent",
        # session_service_builder=session_service_builder,  # Optional.
        enable_tracing=True
    )
    # app._tmpl_attrs["app_name"] = "steering_agent"

    print(f"Before create session")
    session = app.create_session(
        user_id=FLAGS.user_id,  # Required.
        # app_name=agent.name,  # Optional, defaults to agent.name.
        # session_service=session_service_builder(),  # Optional, defaults to InMemorySessionService.
    )
    # session_service = session_service_builder()
    # session = session_service.create_session(app_name=FLAGS.resource_id, user_id=FLAGS.user_id)  # , app_name=agent.name
    # print(f"Created session for user ID: {FLAGS.user_id} - session: {session}")

    for event in app.stream_query(
        user_id=FLAGS.user_id, message="What is the exchange rate from US dollars to Swedish currency on 2025-04-03?",
    ):
        print(event)

    while False:
        user_input = input("Input: ")
        if user_input == "quit":
            break

        for event in app.stream_query(
            user_id=FLAGS.user_id, message=user_input
        ):
            if "content" in event:
                if "parts" in event["content"]:
                    parts = event["content"]["parts"]
                    for part in parts:
                        if "text" in part:
                            text_part = part["text"]
                            print(f"Response: {text_part}")

    app.delete_session(user_id=FLAGS.user_id, session_id=session.id)
    print(f"Deleted session for user ID: {FLAGS.user_id} - session: {session.id}")


if __name__ == "__main__":
    app.run(main)
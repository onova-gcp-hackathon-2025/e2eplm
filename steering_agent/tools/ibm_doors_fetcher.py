import json
import os
from datetime import datetime
import json
import os
from typing import Dict, Any

from google.adk.agents.callback_context import CallbackContext
from google.adk.sessions.state import State
from google.adk.tools import ToolContext

def fetch_requirements_from_ibm_doors(key: str, value: str, tool_context: ToolContext):
    """
    Fetch requirements from IBM DOORS webservice.
    For now, returns mock data from requirements.json.
    Args:
        key: the label indexing the memory to store the value.
        value: the information to be stored.
        tool_context: The ADK tool context.

    Returns:
        A status message.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    mock_path = os.path.join(
        base_dir,
        "..", 
        "..", 
        "third-party", 
        "ibm-doors", 
        "requirements.json"
    )
    with open(os.path.normpath(mock_path), "r", encoding="utf-8") as f:
        requirements = json.load(f)
    mem_dict = tool_context.state
    mem_dict[key] = value
    return {
        "status": f'Stored "{key}": "{value}"',
        "requirements": requirements
    }

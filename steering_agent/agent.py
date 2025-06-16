import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": "The weather in New York is sunny with a temperature of 25°C."
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available."
        }

def get_current_time(city: str) -> dict:
    if city.lower() == "new york":
        tz = ZoneInfo("America/New_York")
        now = datetime.datetime.now(tz)
        return {"status": "success", "report": f"The current time in {city} is {now}."}
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have timezone information for {city}."
        }

root_agent = Agent(
    name="steering_agent",
    model="gemini-2.0-flash",
    description="A simple agent for weather and time queries.",
    tools=[get_weather, get_current_time],
)
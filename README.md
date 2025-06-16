# e2eplm

## Project Setup Instructions

### 1. Set Up the Environment
- **Create and activate a Python virtual environment**:
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
- **Install the Google ADK**:
  ```powershell
  pip install google-adk
  ```

### 2. Create the Project Structure
The project structure is as follows:
```
parent_folder/
    steering_agent/
        __init__.py
        agent.py
        .env
```

### 3. Define the Agent
The `steering_agent` is designed to centralize the workflow between specialized agents. It acts as a coordinator, delegating tasks to specific tools or agents based on the input and ensuring seamless integration of their outputs.

### 4. Set Up the `.env` File
- Add the following to `steering_agent/.env`:
  ```
  GOOGLE_GENAI_USE_VERTEXAI=FALSE
  GOOGLE_API_KEY=YOUR_API_KEY_HERE
  ```

### 5. Run the Agent
- Navigate to the parent directory and launch the agent:
  ```powershell
  cd parent_folder
  adk web
  ```

### 6. Interact with the Agent
- Open the provided URL (e.g., `http://localhost:8000`) in your browser.
- Select the agent and test it with prompts like:
  - "What is the weather in New York?"
  - "What is the time in New York?"
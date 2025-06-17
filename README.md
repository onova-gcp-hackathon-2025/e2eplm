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
  pip install poetry
  poetry install
  ```

### 2. Create the Project Structure
The project structure is as follows:
```
e2eplm/
├── steering_agent/
│   ├── __init__.py
│   ├── agent.py
│   ├── .env
```

### 3. Define the Agent
The `steering_agent` is designed to centralize the workflow between specialized agents. It acts as a coordinator, delegating tasks to specific tools or agents based on the input and ensuring seamless integration of their outputs.

### 4. Set Up the `.env` File (optional)
- Add the following to `steering_agent/.env`:
  ```properties
  GOOGLE_GENAI_USE_VERTEXAI=FALSE
  GOOGLE_API_KEY=YOUR_API_KEY_HERE
  GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
  GOOGLE_CLOUD_LOCATION=us-central1
  GOOGLE_CLOUD_STORAGE_BUCKET=YOUR_BUCKET_NAME
  MODEL=gemini-2.0-flash-001
  ```
- Replace `YOUR_GCP_PROJECT_ID` and `YOUR_BUCKET_NAME` with your actual project ID and bucket name. You can find the project ID in the Google Cloud Console under **Home > Project Info** or by running the following command in the `gcloud` CLI:
  ```powershell
  gcloud config get-value project
  ```

### 5. Run the Agent
- Navigate to the parent directory and launch the agent:
  ```powershell
  cd e2eplm
  adk web
  ```

### 6. Interact with the Agent
- Open the provided URL (e.g., `http://localhost:8000`) in your browser.
- Select the agent and test it with prompts like:
  - "What is the weather in New York?"
  - "What is the time in New York?"

### 7. Miscellaneous / IDE Setup
#### Install Google Cloud Extension for VS Code
1. Open Visual Studio Code.
2. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or pressing `Ctrl+Shift+X`.
3. Search for "Google Cloud Code" and click **Install**.

#### Sign in to Google Cloud in VS Code
1. Open the Command Palette by pressing `Ctrl+P`.
2. Type `Cloud Code: Sign In` and press Enter.
3. Follow the prompts to authenticate with your Google Cloud account.

### 8. Deploy to Google Cloud
#### Prerequisites
1. Install the `gcloud` CLI without admin rights:
   - Download and run the installer using PowerShell:
     ```powershell
     (New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
     & $env:Temp\GoogleCloudSDKInstaller.exe
     ```
   - Follow the prompts in the installer to complete the installation. Ensure the options to add `gcloud` to your `PATH` and start the shell are selected.
   - After installation, verify the installation:
     ```powershell
     gcloud --version
     ```

2. Ensure you are authenticated with Google Cloud:
   ```powershell
   gcloud auth login
   gcloud config set project hacker2025-team-12-dev
   gcloud auth application-default login
   ```

`gcloud auth application-default login` is required for ADC see: https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment

3. Enable required APIs:
   ```powershell
   gcloud services enable run.googleapis.com artifactregistry.googleapis.com
   ```

4. Test the agent locally:
   ```bash
   adk run steering_agent
   ```

#### Steps to Deploy
1. Build the container image:
   ```powershell
   gcloud builds submit --tag gcr.io/hacker2025-team-12-dev/e2eplm
   ```

2. Deploy the container to Cloud Run:
   ```powershell
   gcloud run deploy e2eplm \
       --image gcr.io/hacker2025-team-12-dev/e2eplm \
       --platform managed \
       --region us-central1 \
       --allow-unauthenticated
   ```

3. Note the service URL provided after deployment and use it to access your application.

# ReqPilot by Airquire

> **Elevate Your Requirements, Accelerate Your Flight.**

Welcome to the documentation for **ReqPilot**, Airquire's agentic system for aerospace engineering requirements validation.  
This page is designed for both functional and technical experts who want a rapid, high-level understanding of the project and its value.

---

## What is ReqPilot?

**ReqPilot** automates the validation of complex aerospace requirements, reducing manual effort, accelerating compliance, and minimizing costly rework.  
It leverages Google Cloud Platform (GCP), Vertex AI, and the Google Agent Development Kit (ADK) to ingest, analyze, and cross-reference requirements and engineering responses.

---

## Key Features

- **Automated Requirement Extraction** from PDFs and IBM DOORS
- **Natural Language Understanding** to interpret and refine requirements
- **Gap Analysis** between requirements and engineering responses
- **Validation Reporting** with actionable remediation suggestions
- **Traceability** across all requirement sources and responses

---

## Architecture Overview

<details>
<summary>Click to expand architecture diagram</summary>

![Architecture Diagram](./assets/architecture.png)
</details>

- **Frontend:** Angular + Material UI
- **Backend:** Python, Google ADK, Vertex AI, Cloud Run
- **Data Sources:** IBM DOORS, PDF documents, Cloud Storage

---

## How It Works

1. **Upload** requirements and response documents via the web UI.
2. **Agents** extract, refine, and analyze requirements using Vertex AI.
3. **Gap Analysis** identifies missing, ambiguous, or misaligned requirements.
4. **Validation Report** is generated for engineers to review and act upon.

---

## Quickstart

1. **Clone the repository** and install dependencies:
   ```bash
   git clone https://github.com/airquire/reqpilot.git
   cd reqpilot
   pip install poetry
   poetry install
   ```

2. **Run the agent locally:**
   ```bash
   adk run steering_agent
   ```

3. **Access the web UI:**  
   Open [http://localhost:8000](http://localhost:8000) in your browser.

4. **Deploy to Vertex AI Agent Engine:**  
   See [deployment instructions](../README.md#9-deploy-to-vertex-ai-agent-engine).

---

## Screenshots

Click any thumbnail to enlarge.

| Web UI Home | Upload Dialog | Validation Report |
|:-----------:|:------------:|:----------------:|
| [![Web UI Home](./assets/ui-home-thumb.png)](./assets/ui-home.png) | [![Upload Dialog](./assets/ui-upload-thumb.png)](./assets/ui-upload.png) | [![Validation Report](./assets/ui-report-thumb.png)](./assets/ui-report.png) |

---

## Demo Recording

- [🎬 Watch the full demo (YouTube)](https://youtu.be/your-demo-link)

---

## Further Reading

- [Agentic Hackathon Main Site](https://agentichackathon.onova.io/)
- [ADK Documentation](https://google.github.io/adk-docs/)
- [Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- [Project README](../README.md)

---

*Airquire: Elevate Your Requirements, Accelerate Your Flight.*

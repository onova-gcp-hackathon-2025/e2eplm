# ReqPilot by Airquire

> **Elevate Your Requirements, Accelerate Your Flight.**

Welcome to the documentation for **ReqPilot**, Airquire's agentic system for aerospace engineering requirements validation.  
This page is designed for both functional and technical experts who want a rapid, high-level understanding of the project and its value.

---

## What is ReqPilot?

> **🚀 Elevator Pitch**
>
> **ReqPilot by Airquire** is revolutionizing aerospace engineering compliance by automating requirements validation. Our AI-powered platform ingests complex technical specifications and engineering responses, then uses advanced natural language understanding to identify gaps, misalignments, and ambiguities. Unlike traditional manual processes that take weeks, ReqPilot delivers comprehensive validation in minutes, reducing rework by 60% and accelerating development cycles. With Airquire, aerospace engineers can focus on innovation rather than documentation.


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

See: [README.md](https://github.com/onova-gcp-hackathon-2025/e2eplm/blob/main/README.md)

- **Frontend:** Angular + Material UI
- **Backend:** Python, Google ADK, Vertex AI, Cloud Run
- **Data Sources:** IBM DOORS, PDF documents (synthetic data generated using Vertex AI), Cloud Storage
- **LLMs Models:** [Gemini 2.5 Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro)
- **Deployment:** Vertex AI Agent Engine, Cloud Run, Cloud Storage

---

## How It Works

1. **Upload** requirements and response documents via the web UI.
2. **Agents** extract, refine, and analyze requirements using Vertex AI.
3. **Gap Analysis** identifies missing, ambiguous, or misaligned requirements.
4. **Validation Report** is generated for engineers to review and act upon.

---

## Quickstart

See: [README.md](https://github.com/onova-gcp-hackathon-2025/e2eplm/blob/main/README.md)

1. **Clone the repository** and install dependencies:
2. **Run the agent locally:**
3. **Access the web UI:**  
   Open [http://localhost:8000](http://localhost:8000) in your browser.
4. **Deploy to Vertex AI Agent Engine:**  
   See [deployment instructions](../README.md#9-deploy-to-vertex-ai-agent-engine).
---

## Screenshots

Click any thumbnail to enlarge.

| Capture n°1 | Capture n°2 | Capture n°3 | Capture n°4 |
|:-----------:|:-----------:|:-----------:|:-----------:|
| [![2025-06-20 195016.png](./screencaptures/2025-06-20%20195016.png)](./screencaptures/2025-06-20%20195016.png) | [![2025-06-20 195116.png](./screencaptures/2025-06-20%20195116.png)](./screencaptures/2025-06-20%20195116.png) | [![2025-06-20 195139.png](./screencaptures/2025-06-20%20195139.png)](./screencaptures/2025-06-20%20195139.png) | [![2025-06-20 195155.png](./screencaptures/2025-06-20%20195155.png)](./screencaptures/2025-06-20%20195155.png) |

---

## Demo Recording

[🎬 Agentic Hackathon 2025 - Demo](./recording/Recording-20250623_221045.webm)
<video controls width="720">
  <source src="./recording/Recording-20250623_221045.webm" type="video/webm">
  Your browser does not support the video tag.
</video>

[🎬 Agentic Hackathon 2025 - Demo](./recording/Recording-20250623_221253.webm)
<video controls width="720">
  <source src="./recording/Recording-20250623_221253.webm" type="video/webm">
  Your browser does not support the video tag.
</video>

[🎬 Few shot prompts](./recording/Recording-20250620_201538.webm)
<video controls width="720">
  <source src="./recording/Recording-20250620_201538.webm" type="video/webm">
  Your browser does not support the video tag.
</video>

[🎬 One shot prompt](./recording/Recording-20250623_094911.webm)
<video controls width="720">
  <source src="./recording/Recording-20250623_094911.webm" type="video/webm">
  Your browser does not support the video tag.
</video>

[🎬 Google Cloud Platform infra](./recording/Recording-20250623_095724.webm)
<video controls width="720">
  <source src="./recording/Recording-20250623_095724.webm" type="video/webm">
  Your browser does not support the video tag.
</video>

---

## Further Reading

- [Agentic Hackathon Main Site](https://agentichackathon.onova.io/)
- [ADK Documentation](https://google.github.io/adk-docs/)
- [Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- [Project README](../README.md)

---

*Airquire: Elevate Your Requirements, Accelerate Your Flight.*

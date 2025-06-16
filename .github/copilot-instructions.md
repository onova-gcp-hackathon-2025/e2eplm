# Copilot Custom Instructions

We are a team of two software developers participating in a hackathon.  
Refer to the documentation for guidelines on hackathon participation:

- [Agentic Hackathon Main Site](https://agentichackathon.onova.io/)
- [Agentic Hackathon FAQs](https://agentichackathon.onova.io/faqs)

## Platform & Technology

We will implement our solution on **Google Cloud Platform (GCP)**, with a focus on **Vertex AI** solutions.  
Please use GCP services in all code and architecture suggestions.

### Available GCP Services

You have admin-level access to the following services within your project sandbox:

- **Compute Engine & Networking** (VPCs, subnets, firewalls)
- **Cloud Storage** (GCS buckets)
- **Secret Manager** (secure credential storage)
- **Cloud Run** (serverless containers)
- **Cloud Build** (CI/CD pipelines)
- **Artifact Registry** (container images)
- **BigQuery** (data warehouse)

**Notes:**
- Permissions are scoped to your team’s project only.
- Project-level settings (e.g., billing, project deletion) cannot be modified.
- All actions are logged for security and auditing.

## Implementation Requirements

- Use the **Google Agent Development Kit (ADK)** library in Python.
- Reference materials:
  - [Google ADK Technical Overview](https://medium.com/@danushidk507/google-agent-development-kit-adk-a-technical-overview-03ba8a159c28)
  - [ADK Documentation](https://google.github.io/adk-docs/)
  - [ADK Quickstart](https://google.github.io/adk-docs/get-started/quickstart/)
  - [ADK Samples](https://github.com/google/adk-samples)
  - [ADK Python API Reference](https://google.github.io/adk-docs/api-reference/python/)

## Use Case Description

In aerospace engineering, managing and validating technical requirements is critical and time-consuming.  
Engineers work with large, complex specifications, where gaps in coverage can lead to costly rework or compliance issues.  
Currently, validation is manual and error-prone.

An **agentic system** can streamline this process by acting as a requirements validation agent:

- Ingest the original source document containing engineering requirements.
- Extract and understand the meaning and intent of each requirement.
- Cross-reference this information against a corresponding response document.
- Flag misalignments, omissions, or ambiguities.
- Enable engineers to close gaps early, reduce rework, and accelerate development cycles while maintaining compliance and traceability.

### Functional Parameters

- Ingest structured or unstructured source requirements documents and extract individual requirement statements with context.
- Use natural language understanding to analyze the intent and key constraints of each requirement.
- Ingest and parse the engineering response document (e.g., plans, designs, or test strategies).
- Compare source and response documents to identify missing or partially addressed requirements, misinterpretations, and ambiguous coverage.
- Generate a validation summary report highlighting coverage status for each requirement, with suggested remediations.

**Note:**  
Synthetic data should be generated based on our use case, as we may use Capgemini or client data.

**Assumptions:**  
- Requirements are stored in IBM DOORS.
- Response documents are PDF files.

## Technology Stack

- **Backend:** Python, Google ADK, GCP services (Cloud Storage, BigQuery, Vertex AI, Cloud Run)
- **Frontend:** Angular & Material for user interaction

## Additional Guidance

- Leverage GitHub data retrieval from [google/adk-docs](https://github.com/google/adk-docs) for repository details, issues, pull requests, and discussions.
- Respond with concise code snippets and brief explanations.

Our company name is Airquire.
Slogan: Airquire: Elevate Your Requirements, Accelerate Your Flight.

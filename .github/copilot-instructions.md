# Copilot Custom Instructions
We are a team of 2 software developpers whe are participating in a a hackathon Refer to the documentation at:
- [https://agentichackathon.onova.io/](https://agentichackathon.onova.io/)
- [https://agentichackathon.onova.io/faqs]'https://agentichackathon.onova.io/faqs) for guidelines on hackathon participation. 

We will implement the solution on Google Cloud Paltform GCP and especalily VertexAI solutions.
You should stick to answers that use GCP services.
Here is a a list of services that are avaialble with our GCP project:
"Expanded GCP Access for Your Hackathon Project
Dear Hackathon Participants,
I'm excited to share that we've expanded the administrative capabilities within your team's project sandbox! You now have enhanced access to key Google Cloud Platform (GCP) services—while still maintaining our security boundaries.
🔓 New Administrative Access Includes:
 You now have admin-level access to the following services within your project:
Compute Engine & Networking (VPCs, subnets, firewalls)  
Cloud Storage (GCS buckets)  
Secret Manager (secure credential storage)  
Cloud Run (serverless containers)  
Cloud Build (CI/CD pipelines)  
Artifact Registry (container images)  
BigQuery (data warehouse)
🛠️ What You Can Now Do:
With this expanded access, your team can:
Create and manage VPC networks and firewall rules
Store and manage secrets securely
Deploy and manage Cloud Run services
Set up CI/CD pipelines with Cloud Build
Store and retrieve container images
Create and manage BigQuery datasets and tables
⚠️ Important Notes:
These permissions are scoped to your team’s project only  
You cannot modify project-level settings (e.g., billing, project deletion)  
All actions are logged for security and auditing purposes  
"


I will need to use google adk library to implement the solution in python.
You can refer to those online resources:
- [https://medium.com/@danushidk507/google-agent-development-kit-adk-a-technical-overview-03ba8a159c28](https://medium.com/@danushidk507/google-agent-development-kit-adk-a-technical-overview-03ba8a159c28)
- [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)
- [https://google.github.io/adk-docs/get-started/quickstart/](https://google.github.io/adk-docs/get-started/quickstart/)
- [https://github.com/google/adk-samples](https://github.com/google/adk-samples)
- [https://google.github.io/adk-docs/api-reference/python/](https://google.github.io/adk-docs/api-reference/python/)


Here is a description of our use case to implement:

In aerospace engineering, managing and validating technical requirements is a critical and time-consuming process. Engineers often work with large sets of complex specifications, where even small gaps in coverage can lead to costly rework or compliance issues. Today, validation is typically manual, relying on engineers to read through dense technical documents to ensure response plans fully address the original requirements — a process prone to oversight and inconsistency. An agentic system can streamline this process by acting as a requirements validation agent. It can ingest the original source document containing engineering requirements, extract and understand their meaning and intent, and cross-reference that information against a corresponding response document. The AI agent can then flag any misalignments, omissions, or ambiguities — enabling engineers to close gaps early, reduce rework, and accelerate development cycles while maintaining compliance and traceability.

Parameters:
* Ingest structured or unstructured source requirements documents and extract individual requirement statements with associated context.
* Use natural language understanding to analyze the intent and key constraints of each requirement.
* Ingest and parse the engineering response document (e.g., plans, designs, or test strategies).
* Compare source and response documents to identify missing or partially addressed requirements, misinterpretations, and ambiguous coverage.
* Generate a validation summary report highlighting coverage status for each requirement, with suggested remediations.

We can use capgemini our our client data so we need synthetic data generated based on our use case.

When possible you should imagine the requirement are stored inside IBM DOORS and the response document is a PDF file.

Technology to favor: 
* Use python for implementation, Google Cloud Platform (GCP) services for deployment, and Google Agent Development Kit (ADK) for agentic system development.
* Use Google Cloud Storage for document storage, BigQuery for data analysis, and Vertex AI for machine learning tasks.
* Use Google Cloud Run for deploying the agent as a serverless application.
* Use Angular and Material for the front-end application to interact with the agent.

Imporve response using: 
- @github GitHub Data Retrieval from https://github.com/google/adk-docs repository details
- @github GitHub Data Retrieval from https://github.com/google/adk-docs Open or closed issues
- @github GitHub Data Retrieval from https://github.com/google/adk-docs Pull requests
- @github GitHub Data Retrieval from https://github.com/google/adk-docs Discussions

Respond with concise code snippets and brief explanations.
# Video Pitch Script for AI Hackathon

## Hackathon instructions to create a 3-minute video pitch:

Record a screen share of your team pitching your project, including a technical demo of your project in action.
We suggest using MSFT Teams to screen record. You can share a link to your MSFT Teams video for your submission.
Suggested time breakdown:

First 30 Seconds:Quickly establish the context by outlining the problem you're addressing and your reasons for developing this solution.
Next 2 Minutes:Demo your working AI project. Briefly mention key technologies or notable technical obstacles your team overcame. It's imperative to showcase the actual technical solution to the problem you've identified.
Last 30 seconds:Conclude by making a compelling case - emphasize the potential of your solution and any future aspirations you hold. Include any relevant metrics and your plan for progressing the solution.
Suggestions:

Start with the Problem:Clearly define the problem your AI solution is addressing in the first 20-30 seconds. Make sure the problem is relatable and understandable, especially if it is a technical one. Using a story or a real-world example can help illustrate the issue and draw in your audience.
Explain the Solution:Outline your AI solution, making sure to explain how it addresses the problem you have selected. Be sure to touch on why your solution is unique, the technology used, and any validation (like tests or simulations) that demonstrate its effectiveness. Simplify the technical aspects so anyone can understand, but also be ready to delve into the details for experts in the field.
Demonstrate the Impact:Use data, projections, or case studies to show the positive impacts your solution could have. For example, explain how it could save time, increase efficiency, reduce errors, or otherwise make a significant positive impact. This is your chance to really sell the benefits of your solution.
Visuals and Production Quality:Utilize visuals, animations, and infographics to aid your explanation. This will make your presentation more engaging and help viewers understand complex ideas. Keep in mind the overall production quality of the video, including sound and lighting. A good quality video can convey professionalism and dedication.
Practice and Perfect Your Delivery:Practice your pitch to ensure you can deliver it clearly and confidently within the 3-minute time limit. Your pitch should be enthusiastic but not rushed, making sure to leave time for a strong conclusion that summarizes the key points and leaves a lasting impression. Record multiple takes if necessary and edit for the best result.

## Script

Here’s a 3-minute video script tailored to your context, following the recommended structure and telling a compelling story around the aircraft black box requirement use case:

ReqPilot by Airquire – 3-Minute Video Script
[0:00–0:30] – The Story & Problem

Screen: Team member on camera, with a slide showing a crashed aircraft and a black box.

Speaker:
Imagine this: An aircraft has just suffered a catastrophic accident. Investigators rush to the scene, searching for answers. The only hope for understanding what happened lies in the aircraft’s black box—the flight data recorder. But what if the requirements for recording critical flight parameters were unclear, incomplete, or misunderstood?
In aerospace engineering, every requirement—especially for safety-critical systems like black boxes—must be precise, validated, and traceable. Yet, today, engineers spend weeks manually checking documents, risking gaps that can lead to devastating consequences.

[0:30–2:30] – Demo & Technical Solution

Screen: Switch to a screen share of ReqPilot’s dashboard. Show uploading a DOORS export and a PDF response.

Speaker:
That’s why we built ReqPilot by Airquire. Let’s see how it works.

Here, we upload the original requirements document from IBM DOORS—let’s focus on the black box:
"The flight data recorder shall capture all flight parameters at a minimum frequency of 8Hz and retain data for at least 25 hours."

Next, we upload the engineering response PDF, detailing the design and test plans.

Screen: Show ReqPilot extracting and listing requirements, highlighting the black box requirement.

ReqPilot’s agents, powered by Google’s Agent Development Kit and Vertex AI, automatically extract each requirement and analyze its intent. For our black box, ReqPilot understands the need for continuous, high-frequency data capture and long-term retention.

Screen: Show the gap analysis view. ReqPilot flags a gap: the response document only mentions 4Hz recording frequency.

But here’s the magic: ReqPilot cross-references the response document and instantly flags a misalignment—the engineering plan only records at 4Hz, not the required 8Hz. In a real-world crash, this gap could mean missing vital clues, delaying investigations, or even failing regulatory audits.

Screen: Show the validation report, with the flagged requirement, summary, and suggested remediation.

ReqPilot generates a clear validation report:

Status: Gap detected
Issue: Recording frequency below requirement
Suggested Fix: Update design to meet 8Hz minimum
Engineers can now address this before it becomes a costly or dangerous oversight.

[2:30–3:00] – Impact & Closing

Screen: Return to team member, with a slide showing metrics (e.g., “60% less rework”, “minutes not weeks”).

Speaker:
With ReqPilot, aerospace teams can validate requirements in minutes, not weeks—reducing rework by 60% and ensuring nothing critical slips through the cracks.
Our vision is to make compliance effortless and safety uncompromised, so engineers can focus on innovation, not paperwork.

Closing Slide:
Airquire: Elevate Your Requirements, Accelerate Your Flight.

[End]

This script tells a story, highlights the real-world stakes, and demonstrates ReqPilot’s core value and technical output as described in your instructions.

## Transcript

Imagine this: An aircraft has just suffered a catastrophic accident. Investigators rush to the scene, searching for answers. The only hope for understanding what happened lies in the aircraft’s black box—the flight data recorder. But what if the requirements for recording critical flight parameters were unclear, incomplete, or misunderstood?

In aerospace engineering, every requirement—especially for safety-critical systems like black boxes—must be precise, validated, and traceable. Yet, today, engineers spend weeks manually checking documents, risking gaps that can lead to devastating consequences.

That’s why we built ReqPilot by Airquire. Let’s see how it works.

We can search for the original requirements from IBM DOORS—let’s focus on the black box:
"List the flight data recorder related requirements especially if the data is retained for at least 25 hours."

Next, we search all the engineering PDFs for a mention of such a requirement in the detailed design and test plans, saving us weeks of effort to detect implementation gaps.

ReqPilot’s agents, powered by Google’s Agent Development Kit and Vertex AI, automatically extract each requirement and analyze its intent. For our black box, ReqPilot understands the need for continuous, high-frequency data capture and long-term retention.

But here’s the magic: ReqPilot cross-references the response document and instantly flags a misalignment—the engineering plan that only retain data for 2 hours, not the required 25 hours. In a real-world crash, this gap could mean missing vital clues, delaying investigations, or even failing regulatory audits.

ReqPilot generates a clear validation report about the black box requirement gap detected mentioning an issue in the response recording duration and suggests a fix: Update design to meet 25 hours minimum in the PDF design document mentioning the location and the filename.

Engineers can now address this before it becomes a costly or dangerous oversight.

With ReqPilot, aerospace teams can validate requirements in minutes, not weeks—reducing rework by 60% and ensuring nothing critical slips through the cracks.

Our vision is to make compliance effortless and safety uncompromised, so engineers can focus on innovation, not paperwork.


Technologies Used

ReqPilot is built on Google Cloud Platform (GCP), leveraging Vertex AI for advanced natural language processing and the Google Agent Development Kit (ADK) for agent orchestration. The backend is implemented in Python and deployed on Cloud Run for scalability. All documents are securely stored in Cloud Storage, and the frontend is developed with Angular and Material UI for a modern user experience.

The Agent team is composed of specialized agents, each with a distinct role in the requirements validation process:

Steering Agent:
Acts as the central orchestrator. It receives user inputs, delegates tasks to specialized sub-agents, aggregates their outputs, and ensures a seamless end-to-end validation workflow.

PDFArchivist Agent:
Extracts requirements and relevant data from PDF response documents.

Requirements Curator Agent:
Integrates with IBM DOORS to fetch, curate, and ensure the uniqueness and clarity of requirements.

ReqRefiner Agent:
Enhances and refines requirement statements for quality and compliance.

GapAnalyzer Agent:
Compares source requirements and engineering responses to identify gaps, ambiguities, or misalignments.

ReportGenerator Agent:
Compiles validation results and generates comprehensive summary reports with actionable remediation suggestions.

All agents use the best large language model (gemini 2.5 pro) for consistency and are coordinated by the steering agent to deliver a robust, automated requirements validation solution.

Airquire: Elevate Your Requirements, Accelerate Your Flight.

Thanks for listening
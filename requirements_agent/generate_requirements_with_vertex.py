from vertexai.preview.generative_models import GenerativeModel

import os
import vertexai

vertexai.init(project="hacker2025-team-12-dev", location="us-central1")

model = GenerativeModel("gemini-2.0-flash")

prompt = """
You are an aerospace system engineer. Please generate a list of 5 technical requirements in YAML format 
related to the installation, function, and validation of a flight data recorder (black box) in a commercial aircraft. 
Each requirement must include:
id
title
description
source (e.g., DO-178C, CS-25, internal spec)
priority (High, Medium, Low)
Return only valid YAML content.
"""

response = model.generate_content(prompt)
yaml_content = response.text

# Create output directory if it doesn't exist
output_dir = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(output_dir, exist_ok=True)

# Write to file in output directory
output_file = os.path.join(output_dir, "generated_requirements.yaml")
with open(output_file, "w") as f:
    f.write(yaml_content)

print("✅ Requirements generated and saved to 'generated_requirements.yaml'.")
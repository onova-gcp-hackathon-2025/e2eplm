from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os
import yaml

class RequirementPDFGenerator:
    def __init__(self):
        self.company_name = "Airquire"
        self.aircraft_model = "FlyTest"
        self.logo_path = "media/Airquire-icon2.jpeg"
        
    def load_requirements_from_yaml(self, yaml_file):
        """Load requirements from a YAML file."""
        with open(yaml_file, 'r') as file:
            yaml_content = file.read()
            # Remove backticks if present (for markdown code blocks)
            if yaml_content.strip().startswith('```'):
                yaml_content = '\n'.join(yaml_content.split('\n')[1:-1])
            requirements = yaml.safe_load(yaml_content)
        return requirements
    
    def generate_all_requirements(self, yaml_file, output_dir="requirements_agent/output"):
        """Generate PDFs for all requirements in a YAML file."""
        requirements = self.load_requirements_from_yaml(yaml_file)
        generated_files = []
        
        for req in requirements:
            filename = self.create_requirement_pdf(
                req['id'],
                req['title'],
                req['description'],
                req.get('source', 'N/A'),
                req.get('priority', 'N/A'),
                output_dir
            )
            generated_files.append(filename)
            
        return generated_files
        
    def create_requirement_pdf(self, requirement_id, title, description, source="N/A", priority="N/A", output_dir="requirements_agent/output"):
        """Create a PDF with a complete cartouche for a single requirement."""
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # PDF filename based on requirement ID
        filename = os.path.join(output_dir, f"REQ_{requirement_id}.pdf")
        
        # Create PDF document
        doc = SimpleDocTemplate(
            filename,
            pagesize=landscape(letter),
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50
        )
        
        # Styles
        styles = getSampleStyleSheet()
        
        # Create title style for inside the cartouche
        title_style = ParagraphStyle(
            'ReqTitle',
            parent=styles['Heading1'],
            fontSize=14,
            alignment=0,  # Left aligned
            spaceBefore=0,
            spaceAfter=0,
            textColor=colors.darkblue
        )
        
        header_style = ParagraphStyle(
            'HeaderStyle',
            parent=styles['Heading2'],
            fontSize=12,
            spaceBefore=6,
            spaceAfter=6
        )
        
        normal_style = styles['Normal']
        
        # Content elements
        elements = []
        
        # Add spacer at the top
        elements.append(Spacer(1, 10))
        
        # Format description text properly for table
        desc_paragraph = Paragraph(description, normal_style)
        
        # Prepare the logo
        logo = None
        if os.path.exists(self.logo_path):
            logo = Image(self.logo_path)
            # Set logo size in pixels (1 pixel ≈ 0.75 points)
            logo.drawHeight = 120
            logo.drawWidth = 120
        
        # Format title as a paragraph
        title_paragraph = Paragraph(f"{title}", title_style)
        
        # Create the requirement data table
        data = [
            # Row 1: Logo, Title label, and Title value (3 columns)
            [logo, Paragraph("<b>Title:</b>", header_style), title_paragraph],
        ]
        
        # Add the other rows with their original structure (6 columns)
        data.extend([
            # Row 2: Requirement ID and Priority
            [Paragraph("<b>Requirement ID:</b>", header_style), requirement_id, 
             Paragraph("<b>Priority:</b>", header_style), priority, "", ""],
            # Row 3: Company and Aircraft model
            [Paragraph("<b>Company:</b>", header_style), self.company_name, 
             Paragraph("<b>Aircraft Model:</b>", header_style), self.aircraft_model, "", ""],
            # Row 4: Source
            [Paragraph("<b>Source:</b>", header_style), Paragraph(source, normal_style), "", "", "", ""],
            # Row 5: Description header
            [Paragraph("<b>Description:</b>", header_style), "", "", "", "", ""],
            # Row 6: Description content
            [desc_paragraph, "", "", "", "", ""],
        ])
        
        # Create table without specifying column widths - let it determine based on content
        req_table = Table(data)
        
        # Apply table style with improved spacing
        table_style = TableStyle([
            # Global settings
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            
            # Row 1: Logo, Title label, and Title (3 columns)
            ('SPAN', (0, 0), (0, 0)),  # Logo
            ('BACKGROUND', (1, 0), (1, 0), colors.lightgrey),  # Title label background
            ('SPAN', (2, 0), (5, 0)),  # Title content spans the rest of the row
            ('LEFTPADDING', (0, 0), (0, 0), 10),
            ('RIGHTPADDING', (0, 0), (0, 0), 10),
            ('TOPPADDING', (0, 0), (0, 0), 10),  # Further increased top padding
            ('BOTTOMPADDING', (0, 0), (0, 0), 10),  # Further increased bottom padding
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),  # Center the logo horizontally
            
            # Row 2: Requirement ID and Priority
            ('BACKGROUND', (0, 1), (0, 1), colors.lightgrey),
            ('BACKGROUND', (2, 1), (2, 1), colors.lightgrey),
            ('SPAN', (1, 1), (1, 1)),
            ('SPAN', (3, 1), (5, 1)),
            
            # Row 3: Company and Aircraft model
            ('BACKGROUND', (0, 2), (0, 2), colors.lightgrey),
            ('BACKGROUND', (2, 2), (2, 2), colors.lightgrey),
            ('SPAN', (1, 2), (1, 2)),
            ('SPAN', (3, 2), (5, 2)),
            
            # Row 4: Source
            ('BACKGROUND', (0, 3), (0, 3), colors.lightgrey),
            ('SPAN', (1, 3), (5, 3)),
            
            # Row 5: Description header
            ('BACKGROUND', (0, 4), (0, 4), colors.lightgrey),
            ('SPAN', (0, 4), (5, 4)),
            
            # Row 6: Description content
            ('SPAN', (0, 5), (5, 5)),
            ('VALIGN', (0, 5), (5, 5), 'TOP'),
            ('LEFTPADDING', (0, 5), (0, 5), 12),
            ('RIGHTPADDING', (0, 5), (0, 5), 12),
            ('TOPPADDING', (0, 5), (0, 5), 12),
            ('BOTTOMPADDING', (0, 5), (0, 5), 12),
        ])
        
        req_table.setStyle(table_style)
        
        elements.append(req_table)
        
        # Add footer with date and page number
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=8,
            textColor=colors.gray,
            alignment=1,  # Center alignment
            spaceBefore=30
        )
        
        import datetime
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        footer_text = f"Generated on {current_date} | ReqPilot by Airquire | Elevate Your Requirements, Accelerate Your Flight"
        elements.append(Spacer(1, 30))
        elements.append(Paragraph(footer_text, footer_style))
        
        # Build PDF
        doc.build(elements)
        
        return filename

# Example usage
if __name__ == "__main__":
    generator = RequirementPDFGenerator()
    
    # Path to YAML file
    yaml_file = "c:/Users/qmoneger/Documents/e2eplm/requirements_agent/output/generated_requirements.yaml"
    
    # Generate PDFs for all requirements
    generated_files = generator.generate_all_requirements(yaml_file)
    
    print(f"Generated {len(generated_files)} PDF files:")
    for pdf_file in generated_files:
        print(f" - {pdf_file}")
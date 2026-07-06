from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from io import BytesIO
import re

def clean_text(text):
    # Remove control/non-printable chars
    return re.sub(r'[^\x20-\x7E]', '', text)

def generate_pdf(course_name, roadmap_steps, recommended_websites):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    left_margin = inch
    right_margin = inch
    top_margin = height - inch
    bottom_margin = inch

    text_obj = c.beginText()
    text_obj.setTextOrigin(left_margin, top_margin)
    text_obj.setFont("Helvetica-Bold", 16)
    text_obj.textLine(f"Roadmap for {course_name}")

    text_obj.moveCursor(0, 20)
    text_obj.setFont("Helvetica", 12)
    text_obj.textLine("Step-by-step Roadmap:")

    text_obj.moveCursor(0, 15)
    for idx, step in enumerate(roadmap_steps, 1):
        cleaned_step = clean_text(step).strip()
        # Wrap text at 80 chars approx
        lines = []
        while len(cleaned_step) > 80:
            # Find last space within 80 chars
            space_pos = cleaned_step.rfind(' ', 0, 80)
            if space_pos == -1:
                space_pos = 80
            lines.append(cleaned_step[:space_pos])
            cleaned_step = cleaned_step[space_pos:].strip()
        lines.append(cleaned_step)

        for i, line in enumerate(lines):
            prefix = f"{idx}. " if i == 0 else "    "
            text_obj.textLine(prefix + line)

        text_obj.moveCursor(0, 10)

        # If text goes below margin, add page
        if text_obj.getY() < bottom_margin:
            c.drawText(text_obj)
            c.showPage()
            text_obj = c.beginText()
            text_obj.setTextOrigin(left_margin, top_margin)
            text_obj.setFont("Helvetica", 12)

    text_obj.textLine("")
    text_obj.textLine("Recommended Websites:")
    for site in recommended_websites:
        cleaned_site = clean_text(site)
        text_obj.textLine(f"- {cleaned_site}")

    c.drawText(text_obj)
    c.save()

    buffer.seek(0)

    return buffer
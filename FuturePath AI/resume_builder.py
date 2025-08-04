from fpdf import FPDF

def build_resume(name, summary, skills, education, experience):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt=name, ln=True, align='C')

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Professional Summary", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, summary)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, skills)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, education)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Experience", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, experience)

    pdf.output("resume.pdf")

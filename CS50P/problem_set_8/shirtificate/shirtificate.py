from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", y=60, w=180)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "", 35)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(100)
name = input("Name: ")
pdf = PDF()
pdf.add_page()
pdf.set_text_color(r=255, g=255, b=255)
pdf.set_font("helvetica", "B", 18)
pdf.cell(160, 15, f"{name} took CS50", border=1, center = True, align="C")
pdf.output("shirtificate.pdf")

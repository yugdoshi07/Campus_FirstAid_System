from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from tkinter import messagebox
import os

from database.database import get_all_requests_for_report


def export_requests_pdf():

    data = get_all_requests_for_report()

    file_path = os.path.abspath("Emergency_Requests_Report.pdf")

    pdf = SimpleDocTemplate(file_path)

    table_data = [[
        "ID",
        "Username",
        "Location",
        "Type",
        "Description",
        "Contact",
        "Status"
    ]]

    for row in data:
        table_data.append(list(row))

    table = Table(table_data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ]))

    pdf.build([table])

    print("PDF saved at:", file_path)

    messagebox.showinfo(
        "Success",
        f"PDF Report Exported Successfully!\n\nSaved at:\n{file_path}"
    )
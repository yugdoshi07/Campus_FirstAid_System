import csv
import os
from tkinter import messagebox

from database.database import get_all_requests_for_report


def export_requests_csv():

    data = get_all_requests_for_report()

    file_path = os.path.abspath("Emergency_Requests_Report.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Username",
            "Location",
            "Emergency Type",
            "Description",
            "Contact",
            "Status"
        ])

        writer.writerows(data)

    print("CSV saved at:", file_path)

    messagebox.showinfo(
        "Success",
        f"CSV Report Exported Successfully!\n\nSaved at:\n{file_path}"
    )
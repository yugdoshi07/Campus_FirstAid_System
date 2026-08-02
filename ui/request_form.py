import customtkinter as ctk
from tkinter import messagebox

from database.database import add_request


class RequestForm:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        # Clear Screen
        for widget in root.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(
            root,
            text="🚑 Request First Aid",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        # Location
        self.location = ctk.CTkEntry(
            root,
            width=400,
            placeholder_text="Location"
        )
        self.location.pack(pady=10)

        # Emergency Type
        self.emergency = ctk.CTkComboBox(
            root,
            width=400,
            values=[
                "Injury",
                "Fever",
                "Accident",
                "Burn",
                "Other"
            ]
        )
        self.emergency.pack(pady=10)
        self.emergency.set("Injury")

        # Description
        self.description = ctk.CTkTextbox(
            root,
            width=400,
            height=120
        )
        self.description.pack(pady=10)

        # Contact
        self.contact = ctk.CTkEntry(
            root,
            width=400,
            placeholder_text="Contact Number"
        )
        self.contact.pack(pady=10)

        # Submit Button
        submit = ctk.CTkButton(
            root,
            text="Submit Request",
            command=self.submit_request
        )
        submit.pack(pady=15)

        # Back Button
        back = ctk.CTkButton(
            root,
            text="← Back",
            fg_color="gray",
            command=self.go_back
        )
        back.pack()

    def submit_request(self):

        add_request(
            self.username,
            self.location.get(),
            self.emergency.get(),
            self.description.get("1.0", "end").strip(),
            self.contact.get()
        )

        messagebox.showinfo(
            "Success",
            "First Aid Request Submitted Successfully!"
        )

        from ui.student_dashboard import StudentDashboard
        StudentDashboard(self.root, self.username)


    def go_back(self):
        from ui.student_dashboard import StudentDashboard
        StudentDashboard(self.root, self.username)
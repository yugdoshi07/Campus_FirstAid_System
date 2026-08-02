import customtkinter as ctk
from tkinter import messagebox

from database.database import update_request_status


class UpdateStatus:

    def __init__(self, root, username, request_id):

        self.root = root
        self.username = username
        self.request_id = request_id

        # Clear Screen
        for widget in root.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(
            root,
            text="Update Request Status",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        self.status = ctk.CTkComboBox(
            root,
            values=[
                "Pending",
                "In Progress",
                "Completed"
            ],
            width=250
        )

        self.status.set("Pending")
        self.status.pack(pady=20)

        update_btn = ctk.CTkButton(
            root,
            text="Update Status",
            command=self.update
        )
        update_btn.pack(pady=10)

        back_btn = ctk.CTkButton(
            root,
            text="← Back",
            fg_color="gray",
            command=self.go_back
        )
        back_btn.pack()

    def update(self):

        update_request_status(
            self.request_id,
            self.status.get()
        )

        messagebox.showinfo(
            "Success",
            "Status Updated Successfully!"
        )

        self.go_back()

    def go_back(self):
        from ui.view_requests import ViewRequests
        ViewRequests(self.root, self.username)
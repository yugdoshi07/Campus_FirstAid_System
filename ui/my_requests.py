import customtkinter as ctk

from database.database import get_requests


class MyRequests:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        # Clear Screen
        for widget in root.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(
            root,
            text="📋 My Requests",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        requests = get_requests(username)

        if len(requests) == 0:
            no_data = ctk.CTkLabel(
                root,
                text="No requests found.",
                font=("Arial", 18)
            )
            no_data.pack(pady=20)

        else:

            header = ctk.CTkLabel(
                root,
                text="ID    Location    Type    Status",
                font=("Arial", 18, "bold")
            )
            header.pack(pady=10)

            for req in requests:

                row = ctk.CTkLabel(
                    root,
                    text=f"{req[0]}      {req[1]}      {req[2]}      {req[3]}",
                    font=("Arial", 16)
                )
                row.pack(pady=3)

        back_btn = ctk.CTkButton(
            root,
            text="← Back",
            command=self.go_back
        )
        back_btn.pack(pady=20)

    def go_back(self):
        from ui.student_dashboard import StudentDashboard
        StudentDashboard(self.root, self.username)
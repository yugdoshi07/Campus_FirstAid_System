import customtkinter as ctk
from database.database import get_all_requests
from ui.update_status import UpdateStatus


class ViewRequests:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        # Clear Screen
        for widget in root.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(
            root,
            text="🚑 Emergency Requests",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        requests = get_all_requests()

        if len(requests) == 0:

            no_data = ctk.CTkLabel(
                root,
                text="No Emergency Requests",
                font=("Arial", 18)
            )
            no_data.pack(pady=20)

        else:

            for req in requests:

                card = ctk.CTkFrame(root)
                card.pack(fill="x", padx=20, pady=10)

                info = ctk.CTkLabel(
                    card,
                    text=(
                        f"Request ID : {req[0]}\n"
                        f"Student    : {req[1]}\n"
                        f"Location   : {req[2]}\n"
                        f"Emergency  : {req[3]}\n"
                        f"Description: {req[4]}\n"
                        f"Contact    : {req[5]}\n"
                        f"Status     : {req[6]}"
                    ),
                    justify="left",
                    font=("Arial", 16)
                )
                info.pack(anchor="w", padx=15, pady=10)

                update_btn = ctk.CTkButton(
                    card,
                    text="Update Status",
                    command=lambda request_id=req[0]:
                        UpdateStatus(self.root, self.username, request_id)
                )
                update_btn.pack(pady=(0, 10))

        back_btn = ctk.CTkButton(
            root,
            text="← Back",
            width=200,
            command=self.go_back
        )
        back_btn.pack(pady=20)

    def go_back(self):
        from ui.medical_dashboard import MedicalDashboard
        MedicalDashboard(self.root, self.username)
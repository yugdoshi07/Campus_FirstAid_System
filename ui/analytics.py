import customtkinter as ctk

from database.database import (
    total_users,
    total_requests,
    count_status
)


class Analytics:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        # Clear Screen
        for widget in root.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(
            root,
            text="📊 Analytics Dashboard",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=20)

        users = total_users()
        requests = total_requests()
        pending = count_status("Pending")
        progress = count_status("In Progress")
        completed = count_status("Completed")

        stats = [
            f"👥 Total Users : {users}",
            f"🚑 Total Requests : {requests}",
            f"🟡 Pending : {pending}",
            f"🟠 In Progress : {progress}",
            f"🟢 Completed : {completed}"
        ]

        for item in stats:

            card = ctk.CTkFrame(root)
            card.pack(fill="x", padx=40, pady=8)

            label = ctk.CTkLabel(
                card,
                text=item,
                font=("Arial", 20)
            )
            label.pack(padx=20, pady=15)

        back_btn = ctk.CTkButton(
            root,
            text="← Back",
            fg_color="gray",
            command=self.go_back
        )
        back_btn.pack(pady=30)

    def go_back(self):
        from ui.admin_dashboard import AdminDashboard
        AdminDashboard(self.root, self.username)
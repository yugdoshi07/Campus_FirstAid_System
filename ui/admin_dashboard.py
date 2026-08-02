import customtkinter as ctk

from ui.manage_users import ManageUsers
from ui.analytics import Analytics
from reports.export_csv import export_requests_csv
from reports.export_pdf import export_requests_pdf


class AdminDashboard:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        # Clear Screen
        for widget in root.winfo_children():
            widget.destroy()

        # Main Frame
        main_frame = ctk.CTkFrame(root, corner_radius=15)
        main_frame.pack(expand=True, padx=40, pady=40, fill="both")

        # Title
        title = ctk.CTkLabel(
            main_frame,
            text="👨‍💼 Administrator Dashboard",
            font=("Segoe UI", 34, "bold")
        )
        title.pack(pady=(30, 10))

        # Welcome
        welcome = ctk.CTkLabel(
            main_frame,
            text=f"Welcome, {self.username}",
            font=("Segoe UI", 20)
        )
        welcome.pack(pady=(0, 30))

        # Manage Users
        users_btn = ctk.CTkButton(
            main_frame,
            text="👥 Manage Users",
            width=320,
            height=50,
            corner_radius=12,
            font=("Segoe UI", 18, "bold"),
            command=self.manage_users
        )
        users_btn.pack(pady=12)

        # Manage Requests
        requests_btn = ctk.CTkButton(
            main_frame,
            text="🚑 Manage Requests",
            width=320,
            height=50,
            corner_radius=12,
            font=("Segoe UI", 18, "bold"),
            command=self.manage_requests
        )
        requests_btn.pack(pady=12)

        # Analytics
        analytics_btn = ctk.CTkButton(
            main_frame,
            text="📊 Analytics",
            width=320,
            height=50,
            corner_radius=12,
            font=("Segoe UI", 18, "bold"),
            command=self.analytics
        )
        analytics_btn.pack(pady=12)

        # Reports
        reports_btn = ctk.CTkButton(
            main_frame,
            text="📄 Export Reports",
            width=320,
            height=50,
            corner_radius=12,
            font=("Segoe UI", 18, "bold"),
            command=self.reports
        )
        reports_btn.pack(pady=12)

        # Logout
        logout_btn = ctk.CTkButton(
            main_frame,
            text="🚪 Logout",
            width=320,
            height=50,
            corner_radius=12,
            font=("Segoe UI", 18, "bold"),
            fg_color="red",
            hover_color="darkred",
            command=self.logout
        )
        logout_btn.pack(pady=(30, 20))

    def manage_users(self):
        ManageUsers(self.root, self.username)

    def manage_requests(self):
        from ui.view_requests import ViewRequests
        ViewRequests(self.root, self.username)

    def analytics(self):
        Analytics(self.root, self.username)

    def reports(self):
        export_requests_csv()
        export_requests_pdf()

    def logout(self):
        from ui.welcome import WelcomePage
        WelcomePage(self.root)
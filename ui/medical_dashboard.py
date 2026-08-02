import customtkinter as ctk


class MedicalDashboard:

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
            text="👨‍⚕️ Medical Staff Dashboard",
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

        # View Requests
        requests_btn = ctk.CTkButton(
            main_frame,
            text="🚑 View Emergency Requests",
            width=320,
            height=50,
            corner_radius=12,
            font=("Segoe UI", 18, "bold"),
            command=self.view_requests
        )
        requests_btn.pack(pady=12)

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

    def view_requests(self):
        from ui.view_requests import ViewRequests
        ViewRequests(self.root, self.username)

    def logout(self):
        from ui.welcome import WelcomePage
        WelcomePage(self.root)
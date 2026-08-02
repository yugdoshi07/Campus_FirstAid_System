import customtkinter as ctk
from tkinter import messagebox
from ui.request_form import RequestForm


class StudentDashboard:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        # Clear previous screen
        for widget in root.winfo_children():
            widget.destroy()

        # Main Frame
        main_frame = ctk.CTkFrame(root, corner_radius=15)
        main_frame.pack(expand=True, padx=40, pady=40, fill="both")

        # Title
        title = ctk.CTkLabel(
            main_frame,
            text="🎓 Student Dashboard",
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

        # Request First Aid
        request_btn = ctk.CTkButton(
            main_frame,
            text="🚑 Request First Aid",
            width=320,
            height=50,
            corner_radius=12,
            font=("Segoe UI", 18, "bold"),
            command=self.open_request_form
        )
        request_btn.pack(pady=12)

        # My Requests
        history_btn = ctk.CTkButton(
            main_frame,
            text="📋 My Requests",
            width=320,
            height=50,
            corner_radius=12,
            font=("Segoe UI", 18, "bold"),
            command=self.my_requests
        )
        history_btn.pack(pady=12)

        # Profile
        profile_btn = ctk.CTkButton(
            main_frame,
            text="👤 Profile",
            width=320,
            height=50,
            corner_radius=12,
            font=("Segoe UI", 18, "bold"),
            command=self.profile
        )
        profile_btn.pack(pady=12)

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

    def open_request_form(self):
        RequestForm(self.root, self.username)

    def my_requests(self):
        messagebox.showinfo(
            "My Requests",
            "This feature is already implemented.\nWe'll connect it to the dashboard next."
        )

    def profile(self):
        messagebox.showinfo(
            "Profile",
            f"Username: {self.username}\nRole: Student"
        )

    def logout(self):
        from ui.welcome import WelcomePage
        WelcomePage(self.root)
import customtkinter as ctk
from tkinter import messagebox
from database.database import check_login


class LoginPage:

    def __init__(self, root, role):

        self.root = root
        self.role = role

        # Clear current screen
        for widget in root.winfo_children():
            widget.destroy()

        # Left Panel
        left = ctk.CTkFrame(root, width=400, corner_radius=0)
        left.pack(side="left", fill="y")

        title = ctk.CTkLabel(
            left,
            text="Campus\nFirst-Aid\nRequest System",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=80)

        # Right Panel
        right = ctk.CTkFrame(root, corner_radius=0)
        right.pack(expand=True, fill="both")

        heading = ctk.CTkLabel(
            right,
            text=f"{role} Login",
            font=("Arial", 30, "bold")
        )
        heading.pack(pady=40)

        # Username Entry
        self.username = ctk.CTkEntry(
            right,
            width=300,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        # Password Entry
        self.password = ctk.CTkEntry(
            right,
            width=300,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        # Login Button
        login_btn = ctk.CTkButton(
            right,
            text="Login",
            width=180,
            height=40,
            command=self.login
        )
        login_btn.pack(pady=(20, 10))

        # Back Button
        back_btn = ctk.CTkButton(
            right,
            text="← Back",
            width=180,
            height=40,
            fg_color="gray",
            hover_color="darkgray",
            command=self.go_back
        )
        back_btn.pack()

    def login(self):

        username = self.username.get()
        password = self.password.get()

        user = check_login(username, password, self.role)

        # Debug output
        print("Role:", self.role)
        print("Username:", username)
        print("Database Result:", user)

        if user:

            if self.role == "Student":
                from ui.student_dashboard import StudentDashboard
                StudentDashboard(self.root, username)

            elif self.role == "Medical Staff":
                from ui.medical_dashboard import MedicalDashboard
                MedicalDashboard(self.root, username)

            elif self.role == "Administrator":
                from ui.admin_dashboard import AdminDashboard
                AdminDashboard(self.root, username)

        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid Username, Password or Role"
            )

    def go_back(self):
        from ui.welcome import WelcomePage
        WelcomePage(self.root)
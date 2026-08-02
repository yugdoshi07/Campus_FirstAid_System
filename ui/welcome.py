import customtkinter as ctk
from ui.login import LoginPage
from PIL import Image


class WelcomePage:

    def __init__(self, root):

        self.root = root

        # Clear previous screen
        for widget in root.winfo_children():
            widget.destroy()

        # Left Panel
        left = ctk.CTkFrame(root, width=450, corner_radius=0)
        left.pack(side="left", fill="y")

        # Logo
        logo = ctk.CTkImage(
            light_image=Image.open("assets/logo.png"),
            dark_image=Image.open("assets/logo.png"),
            size=(180, 180)
        )

        logo_label = ctk.CTkLabel(
            left,
            image=logo,
            text=""
        )
        logo_label.pack(pady=(40, 20))

        # Project Title
        title = ctk.CTkLabel(
            left,
            text="Campus\nFirst-Aid\nRequest System",
            font=("Arial", 32, "bold")
        )
        title.pack()

        # Description
        desc = ctk.CTkLabel(
            left,
            text="Helping Students During\nMedical Emergencies",
            font=("Arial", 18)
        )
        desc.pack(pady=20)

        # Right Panel
        right = ctk.CTkFrame(root, corner_radius=0)
        right.pack(expand=True, fill="both")

        heading = ctk.CTkLabel(
            right,
            text="Welcome",
            font=("Arial", 34, "bold")
        )
        heading.pack(pady=50)

        info = ctk.CTkLabel(
            right,
            text="Select your role to continue",
            font=("Arial", 18)
        )
        info.pack(pady=10)

        # Student Button
        student_btn = ctk.CTkButton(
            right,
            text="🎓 Student",
            width=250,
            height=45,
            command=lambda: LoginPage(root, "Student")
        )
        student_btn.pack(pady=15)

        # Medical Staff Button
        staff_btn = ctk.CTkButton(
            right,
            text="👨‍⚕️ Medical Staff",
            width=250,
            height=45,
            command=lambda: LoginPage(root, "Medical Staff")
        )
        staff_btn.pack(pady=15)

        # Administrator Button
        admin_btn = ctk.CTkButton(
            right,
            text="👨‍💼 Administrator",
            width=250,
            height=45,
            command=lambda: LoginPage(root, "Administrator")
        )
        admin_btn.pack(pady=15)
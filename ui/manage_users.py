import customtkinter as ctk
from tkinter import messagebox

from database.database import get_all_users, add_user, delete_user
from ui.edit_user import EditUser


class ManageUsers:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        # Clear Screen
        for widget in root.winfo_children():
            widget.destroy()

        # Title
        title = ctk.CTkLabel(
            root,
            text="👥 Manage Users",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        # Username
        self.user_entry = ctk.CTkEntry(
            root,
            width=300,
            placeholder_text="Username"
        )
        self.user_entry.pack(pady=8)

        # Password
        self.pass_entry = ctk.CTkEntry(
            root,
            width=300,
            placeholder_text="Password",
            show="*"
        )
        self.pass_entry.pack(pady=8)

        # Role
        self.role = ctk.CTkComboBox(
            root,
            values=[
                "Student",
                "Medical Staff",
                "Administrator"
            ],
            width=300
        )
        self.role.set("Student")
        self.role.pack(pady=8)

        # Add User Button
        add_btn = ctk.CTkButton(
            root,
            text="➕ Add User",
            command=self.add_new_user
        )
        add_btn.pack(pady=15)

        # Header
        header = ctk.CTkLabel(
            root,
            text="Users",
            font=("Arial", 20, "bold")
        )
        header.pack(pady=10)

        # User List
        users = get_all_users()

        for user in users:

            card = ctk.CTkFrame(root)
            card.pack(fill="x", padx=20, pady=8)

            info = ctk.CTkLabel(
                card,
                text=(
                    f"ID: {user[0]}\n"
                    f"Username: {user[1]}\n"
                    f"Password: {user[2]}\n"
                    f"Role: {user[3]}"
                ),
                justify="left",
                font=("Arial", 16)
            )
            info.pack(side="left", padx=15, pady=10)

            button_frame = ctk.CTkFrame(card, fg_color="transparent")
            button_frame.pack(side="right", padx=15)

            edit_btn = ctk.CTkButton(
                button_frame,
                text="✏️ Edit",
                width=80,
                command=lambda selected_user=user: self.edit_selected_user(selected_user)
            )
            edit_btn.pack(pady=5)

            delete_btn = ctk.CTkButton(
                button_frame,
                text="❌ Delete",
                width=80,
                fg_color="red",
                hover_color="darkred",
                command=lambda user_id=user[0]: self.delete_selected_user(user_id)
            )
            delete_btn.pack(pady=5)

        # Back Button
        back_btn = ctk.CTkButton(
            root,
            text="← Back",
            fg_color="gray",
            command=self.go_back
        )
        back_btn.pack(pady=20)

    def add_new_user(self):

        try:
            add_user(
                self.user_entry.get(),
                self.pass_entry.get(),
                self.role.get()
            )

            messagebox.showinfo(
                "Success",
                "User Added Successfully!"
            )

            ManageUsers(self.root, self.username)

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def edit_selected_user(self, user):
        EditUser(self.root, self.username, user)

    def delete_selected_user(self, user_id):

        if user_id in [1, 2, 3]:
            messagebox.showwarning(
                "Protected User",
                "Default users (student, doctor, admin) cannot be deleted."
            )
            return

        delete_user(user_id)

        messagebox.showinfo(
            "Success",
            "User Deleted Successfully!"
        )

        ManageUsers(self.root, self.username)

    def go_back(self):
        from ui.admin_dashboard import AdminDashboard
        AdminDashboard(self.root, self.username)
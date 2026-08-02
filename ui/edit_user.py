import customtkinter as ctk
from tkinter import messagebox

from database.database import update_user


class EditUser:

    def __init__(self, root, admin_username, user):

        self.root = root
        self.admin_username = admin_username
        self.user_id = user[0]

        for widget in root.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(
            root,
            text="✏️ Edit User",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        self.username = ctk.CTkEntry(root, width=300)
        self.username.insert(0, user[1])
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(root, width=300)
        self.password.insert(0, user[2])
        self.password.pack(pady=10)

        self.role = ctk.CTkComboBox(
            root,
            values=["Student", "Medical Staff", "Administrator"],
            width=300
        )
        self.role.set(user[3])
        self.role.pack(pady=10)

        update_btn = ctk.CTkButton(
            root,
            text="Update User",
            command=self.update
        )
        update_btn.pack(pady=20)

        back_btn = ctk.CTkButton(
            root,
            text="← Back",
            fg_color="gray",
            command=self.go_back
        )
        back_btn.pack()

    def update(self):

        update_user(
            self.user_id,
            self.username.get(),
            self.password.get(),
            self.role.get()
        )

        messagebox.showinfo(
            "Success",
            "User Updated Successfully!"
        )

        self.go_back()

    def go_back(self):
        from ui.manage_users import ManageUsers
        ManageUsers(self.root, self.admin_username)
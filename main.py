import customtkinter as ctk
import database.database
from ui.welcome import WelcomePage

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Campus First-Aid Request System")
app.geometry("1200x720")
app.minsize(1000, 600)

WelcomePage(app)

app.mainloop()
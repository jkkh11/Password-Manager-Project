import customtkinter as ctk # type: ignore
import jpt.tkinter_design.gui.sidebar.button as btn

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("600x400")
root.title("JPT")
sidebar = ctk.CTkFrame(root, width=150, corner_radius=0)
sidebar.pack(side="left", fill="y")  

content_frame = ctk.CTkFrame(root, corner_radius=10)
content_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

sidebar_title = ctk.CTkLabel(sidebar, text = "JPT", font = ("Arial", 20, "bold"))
sidebar_title.pack(padx=10,pady = 5)

button1 = ctk.CTkButton(sidebar, text="Password generator", command=lambda: btn.button1(content_frame), fg_color = "#302c2c", corner_radius = 0)
button1.pack(fill = "both")

button2 = ctk.CTkButton(sidebar, text="Passphrase generator", command=lambda: btn.button2(content_frame), fg_color = "#302c2c", corner_radius = 0)
button2.pack(fill = "both")

button3 = ctk.CTkButton(sidebar, text="Password strength", command=lambda: btn.button3(content_frame), fg_color = "#302c2c", corner_radius = 0)
button3.pack(fill = "both")

button4 = ctk.CTkButton(sidebar, text="Data breach search", command=lambda: btn.button4(content_frame), fg_color = "#302c2c", corner_radius = 0)
button4.pack(fill = "both")

button5 = ctk.CTkButton(sidebar, text="Manager", command=lambda: btn.button6(content_frame), fg_color = "#302c2c", corner_radius = 0)
button5.pack(fill = "both")

button6 = ctk.CTkButton(sidebar, text="About", command=lambda: btn.button5(content_frame), fg_color = "#302c2c", corner_radius = 0)
button6.pack(fill = "both")



def init():
    root.mainloop()

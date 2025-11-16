import customtkinter as ctk

def edit_password(x,u,p):
    entry = None
    def add():
        nonlocal entry
        entry = entry2.get(),entry3.get()
        root.destroy()

    root = ctk.CTkToplevel(x)
    root.title("Edit password")

    root.geometry("160")

    label2 = ctk.CTkLabel(root,text = "New Username:")
    label2.grid(row=0,column = 0, padx=10,pady=5)

    label3 = ctk.CTkLabel(root,text = "New Password:")
    label3.grid(row=1,column = 0, padx=10,pady=5)

    entry2 = ctk.CTkEntry(root, placeholder_text=u)
    entry2.grid(row=0, column=1, padx=10, pady=5)

    entry3 = ctk.CTkEntry(root, placeholder_text= p)
    entry3.grid(row=1, column=1, padx=10, pady=5)

    close_button = ctk.CTkButton(root, text="Submit", command=add)
    close_button.grid(row=3, column=1, padx=10, pady=10)

    x.wait_window(root)

    return entry



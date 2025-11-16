import customtkinter as ctk

def add_pswd(x):
    entry = None
    def add():
        nonlocal entry
        entry = entry1.get(),entry2.get(),entry3.get()
        root.destroy()

    root = ctk.CTkToplevel(x)
    root.title("Enter password")

    root.geometry("300x170")

    label1 = ctk.CTkLabel(root,text = "Enter Service:")
    label1.grid(row=0,column = 0, padx=10,pady=5)

    label2 = ctk.CTkLabel(root,text = "Enter Username:")
    label2.grid(row=1,column = 0, padx=10,pady=5)

    label3 = ctk.CTkLabel(root,text = "Enter Password:")
    label3.grid(row=2,column = 0, padx=10,pady=5)

    entry1 = ctk.CTkEntry(root)
    entry1.grid(row=0, column=1, padx=10, pady=5)

    entry2 = ctk.CTkEntry(root)
    entry2.grid(row=1, column=1, padx=10, pady=5)

    entry3 = ctk.CTkEntry(root)
    entry3.grid(row=2, column=1, padx=10, pady=5)

    close_button = ctk.CTkButton(root, text="Submit", command=add)
    close_button.grid(row=3, column=1, padx=10, pady=10)

    x.wait_window(root)
    
    if entry == ("","",""):
        return None
    
    return entry



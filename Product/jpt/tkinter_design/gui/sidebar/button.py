import customtkinter as ctk # type: ignore
import jpt.generator.password as pswd
import jpt.generator.passphrase as psph
import jpt.password_checker.password_check as zxcvbn
import jpt.data_breach.breach_searcher as breach
import jpt.manager.manager as manager
import jpt.manager.add_password.add_password as add_password
import jpt.manager.edit_password.edit_password as edit_password
import os

def clear(x):
    for widget in x.winfo_children():
        widget.destroy()

def button1(x):
    clear(x)
    label_button1 = ctk.CTkLabel(x, text = "Password Generator",corner_radius=10, fg_color = "transparent", font = ("Kozuka Gothic Pr6N H",20))
    label_button1.pack(pady=5)

    option_label1 = ctk.CTkLabel(x, text = "Options:", font = ("Kozuka Gothic Pr6N H",14))
    option_label1.pack(pady=5)

    option_frame_1 = ctk.CTkFrame(x,corner_radius=10, height = 100)
    option_frame_1.pack(fill = "both",padx = 50)

    check_var1 = ctk.BooleanVar(value = True)
    check_var2 = ctk.BooleanVar()
    check_var3 = ctk.BooleanVar()
    check_var4 = ctk.BooleanVar()
    
    checkbox1 = ctk.CTkCheckBox(option_frame_1, text="Lowercase",variable=check_var1)
    checkbox1.grid(column = 0, row = 0,pady = 10, padx = 20)

    checkbox2 = ctk.CTkCheckBox(option_frame_1, text="Uppercase", variable=check_var2)
    checkbox2.grid(column = 0, row = 1,pady = 10, padx = 20)

    checkbox3 = ctk.CTkCheckBox(option_frame_1, text="Numbers", variable=check_var3)
    checkbox3.grid(column = 1, row = 0, pady = 10, padx = 20)

    checkbox4 = ctk.CTkCheckBox(option_frame_1, text="Symbols", variable=check_var4)
    checkbox4.grid(column = 1, row = 1, pady = 10, padx = 20)

    sliderframe_1 = ctk.CTkFrame(x, corner_radius = 10)
    sliderframe_1.pack(fill = "both", padx = 10, pady = 10)

    slider_label1 = ctk.CTkLabel(sliderframe_1, text = "Password length:")
    slider_label1.grid(column = 0, row = 0, padx = 10, pady = 10, sticky = "w")

    def update_label1(x):
        slider_label1_2.configure(text = str(int(x)))

    slider1 = ctk.CTkSlider(sliderframe_1, from_=8, to = 20, command = update_label1, number_of_steps = 12)
    slider1.grid(column = 1, row = 0, sticky = "w")
    slider1.set(8)

    slider_label1_2 = ctk.CTkLabel(sliderframe_1, text = "8")
    slider_label1_2.grid(column = 2, row = 0, sticky = "e", padx = 10)

    final_frame = ctk.CTkFrame(x, fg_color = "transparent")
    final_frame.pack(padx = 10, pady = 10, fill = "both")

    def generate():
        uppercase = check_var1.get()
        lowercase = check_var2.get() 
        digits = check_var3.get() 
        symbols = check_var4.get()
        length = int(slider1.get())
        if pswd.generate(length,uppercase,lowercase,digits,symbols) == None:
            output_label.configure(text = "Please select one option")
        output_label.configure(text=pswd.generate(length,uppercase,lowercase,digits,symbols))


    generate_button = ctk.CTkButton(final_frame, text = "Generate!", command = generate)
    generate_button.grid(column = 0, row = 0, padx = 10, pady = 10)

    output_label = ctk.CTkLabel(final_frame, text = "                                  ", font = ("Kozuka Gothic Pr6N H", 14, "bold"), bg_color = "#292929", corner_radius=10)
    output_label.grid(column = 1, row = 0, padx = 10, pady = 10, sticky = "e")

def button2(x):
    clear(x)
    label_button1 = ctk.CTkLabel(x, text = "Passphrase Generator",corner_radius=10, fg_color = "transparent", font = ("Kozuka Gothic Pr6N H",20))
    label_button1.pack(pady=5)

    option_label1 = ctk.CTkLabel(x, text = "Options:", font = ("Arial",14))
    option_label1.pack(pady=5)

    option_frame_1 = ctk.CTkFrame(x,corner_radius=10, height = 100)
    option_frame_1.pack(fill = "both",padx = 10)

    check_var1 = ctk.BooleanVar(value = True)
    check_var2 = ctk.BooleanVar()
    check_var3 = ctk.BooleanVar()

    checkbox1 = ctk.CTkCheckBox(option_frame_1, text="Uppercase",variable = check_var1)
    checkbox1.grid(column = 0, row = 0,pady = 10, padx = 10)

    checkbox2 = ctk.CTkCheckBox(option_frame_1, text="Numbers", variable = check_var2)
    checkbox2.grid(column = 1, row = 0,pady = 10, padx = 10)

    checkbox3 = ctk.CTkCheckBox(option_frame_1, text="Delimiters", variable = check_var3)
    checkbox3.grid(column = 2, row = 0, pady = 10, padx = 10)

    sliderframe_1 = ctk.CTkFrame(x, corner_radius = 10)
    sliderframe_1.pack(fill = "both", padx = 10, pady = 10)

    slider_label1 = ctk.CTkLabel(sliderframe_1, text = "Passphrase length:")
    slider_label1.grid(column = 0, row = 0, padx = 10, pady = 10, sticky = "w")

    def update_label1(x):
        slider_label1_2.configure(text = str(int(x)))

    slider1 = ctk.CTkSlider(sliderframe_1, from_=3, to = 10, command = update_label1, number_of_steps = 7)
    slider1.grid(column = 1, row = 0, sticky = "w")
    slider1.set(3)

    slider_label1_2 = ctk.CTkLabel(sliderframe_1, text = "3")
    slider_label1_2.grid(column = 2, row = 0, sticky = "e", padx = 10)



    def generate():
        caps = check_var1.get()
        digits = check_var2.get()
        delimiter = check_var3.get()
        length = int(slider1.get())
        output_label.configure(text=psph.generate(length,caps, digits, delimiter))    

    generate_button = ctk.CTkButton(x, text = "Generate!", command = generate)
    generate_button.pack(padx = 10, pady = 10)
    output_label = ctk.CTkLabel(x, text = "                                  ", font = ("Kozuka Gothic Pr6N H", 14, "bold"),bg_color = "#292929", wraplength = 380, corner_radius=10)
    output_label.pack(padx = 10, pady = 10)

def button3(x):
    clear(x)
    label_button3 = ctk.CTkLabel(x, text = "Password strength checker",corner_radius=10, fg_color = "transparent", font = ("Kozuka Gothic Pr6N H",20))
    label_button3.pack(pady=20)
    
    entry_frame = ctk.CTkFrame(x, corner_radius = 10)
    entry_frame.pack(padx = 10, fill = "both")

    entry_label = ctk.CTkLabel(entry_frame, text = "Enter your password here:", font = ("Kozuka Gothic Pr6N H",14))
    entry_label.grid(column = 0, row = 0, padx = 10, pady = 10)

    entry_box = ctk.CTkEntry(entry_frame, corner_radius = 3, placeholder_text= "Password")
    entry_box.grid(column = 1, row = 0, padx = 10, pady = 10)

    def feedback():
        if zxcvbn.check_password(str(entry_box.get())) != None:
            feedback_label.configure(text=zxcvbn.check_password(str(entry_box.get())))
        else:
            feedback_label.configure(text="Please enter a password")

    submit_button = ctk.CTkButton(x, text = "Submit", command = feedback)
    submit_button.pack(padx = 10, pady = 10)

    feedback_frame = ctk.CTkFrame(x, corner_radius=10)
    feedback_frame.pack(fill = "both", padx = 10, pady = 10)

    feedback_label = ctk.CTkLabel(feedback_frame, font = ("Kozuka Gothic Pr6N H",14), wraplength = 380, justify = "left",text = "")
    feedback_label.pack(padx = 10, pady= 10,fill = "both")



def button4(x):
    clear(x)
    label_button4 = ctk.CTkLabel(x, text = "Has your password been breached?",corner_radius=10, fg_color = "transparent",font = ("Kozuka Gothic Pr6N H",18))
    label_button4.pack(pady=20)

    entry_frame = ctk.CTkFrame(x, corner_radius = 10)
    entry_frame.pack(padx = 10, fill = "both")

    entry_label = ctk.CTkLabel(entry_frame, text = "Enter your password here:", font = ("Kozuka Gothic Pr6N H",14))
    entry_label.grid(column = 0, row = 0, padx = 5, pady = 10)

    entry_box = ctk.CTkEntry(entry_frame, corner_radius = 3, placeholder_text= "Password")
    entry_box.grid(column = 1, row = 0, padx = 5, pady = 10)

    feedback_frame = ctk.CTkFrame(x, corner_radius=10)
    feedback_frame.pack(fill = "both", padx = 10, pady = 10)

    feedback_label = ctk.CTkLabel(feedback_frame,font = ("Kozuka Gothic Pr6N H",14), wraplength = 380, justify = "left",text = "")
    feedback_label.pack(padx = 10, pady = 10, fill = "both")

    def feedback():
        if breach.breach_search(entry_box.get()) != None: 
            feedback_label.configure(text=f'The password \"{entry_box.get()}\" has appeared in a data breach {breach.breach_search(entry_box.get())} times.')
        else:
            feedback_label.configure(text="Please enter a password")

    submit_button = ctk.CTkButton(x, text = "Submit", command = feedback)
    submit_button.pack(padx = 10, pady = 10)

def button5(x):
    clear(x)
    label_button4 = ctk.CTkLabel(x, text = "About",corner_radius=10, fg_color = "transparent",font = ("Kozuka Gothic Pr6N H",20))
    label_button4.pack(pady=20,padx = 20)

    about_frame = ctk.CTkFrame(x, corner_radius = 10, height = 120)
    about_frame.pack(padx=25,pady=10,fill = "x")
    about_label = ctk.CTkLabel(about_frame, text = "Joshua's Password Tool (JPT)\n Version 1.0.0")
    about_label.pack(padx=10,pady=10)

def create_password(x):
    label_button4 = ctk.CTkLabel(x, text = "System Password Setup",corner_radius=10, fg_color = "transparent",font = ("Kozuka Gothic Pr6N H",20))
    label_button4.pack(pady=20,padx = 20)

    create_pswd_frame = ctk.CTkFrame(x, corner_radius = 10, height = 120)
    create_pswd_frame.pack(padx=25,pady=10,fill = "x")

    create_pswd_label = ctk.CTkLabel(create_pswd_frame, text = "Enter your password:",corner_radius = 10)
    create_pswd_label.grid(row = 0,column = 0, padx=10,pady=10)

    pswd_entry = ctk.CTkEntry(create_pswd_frame, corner_radius = 10)
    pswd_entry.grid(column = 1, row = 0, sticky = "e")

    confirm_pswd_label = ctk.CTkLabel(create_pswd_frame, text = "Confirm your password:",corner_radius = 10)
    confirm_pswd_label.grid(row = 1,column = 0, padx=10,pady=10)

    confirm_entry = ctk.CTkEntry(create_pswd_frame, corner_radius = 10)
    confirm_entry.grid(column = 1, row = 1, sticky = "e")

    feedback_label = ctk.CTkLabel(x,corner_radius = 10, text = "")
    feedback_label.pack(padx=10,pady=10)
    def system_setup():
        if manager.create_system_pswd(pswd_entry.get(),confirm_entry.get()) == False:
            feedback_label.configure(text="Not the same password")
        else:
            feedback_label.configure(text="")
            login_screen(x)



    submit_button = ctk.CTkButton(x,text="Submit",corner_radius = 10, command=system_setup)
    submit_button.pack(padx=10,pady=10)

def pswd_manager(x):
    clear(x)
    key = manager.encrypt_setup()
    cipher = manager.Fernet(key)
    passwords = manager.load(cipher)
    
    label_button = ctk.CTkLabel(x, text = "Password Manager",corner_radius=10, fg_color = "transparent",font = ("Kozuka Gothic Pr6N H",20))
    label_button.pack(padx=10,pady=10)

    def add_pwd():
        new_password = add_password.add_pswd(x)
        if new_password != None:
            manager.add(passwords,new_password[0],new_password[1],new_password[2])
            manager.save(passwords, cipher)
            show_passwords()

    add_button = ctk.CTkButton(x,text="add password", corner_radius = 10, command = add_pwd)
    add_button.pack()

    password_list_frame = ctk.CTkScrollableFrame(x, corner_radius=10)
    password_list_frame.pack(padx=10,pady=10,fill="x")
    
    def titles():
        service_title = ctk.CTkLabel(password_list_frame, text = "Services", font = ("Kozuka Gothic Pr6N H",13,"bold"))
        service_title.grid(row=0,column=0,padx=10,pady=0)
        user_title = ctk.CTkLabel(password_list_frame, text = "Username", font = ("Kozuka Gothic Pr6N H",13,"bold"))
        user_title.grid(row=0,column=1,padx=10,pady=0)
        password_title = ctk.CTkLabel(password_list_frame, text = "Passwords", font = ("Kozuka Gothic Pr6N H",13,"bold"))
        password_title.grid(row=0,column=2, padx=10,pady=0)

    

    def delete(r):
        services_listed = list(passwords.keys())
        manager.delete(passwords,services_listed[r-1])
        manager.save(passwords,cipher)
        for widget in password_list_frame.winfo_children():
            widget.destroy()
        show_passwords()
    
    def edit(r):
        services_listed = list(passwords.keys())
        update_password = edit_password.edit_password(x,passwords[services_listed[r-1]]["username"], passwords[services_listed[r-1]]["password"])
        if update_password != None:
            manager.update(passwords,services_listed[r-1], update_password[0],update_password[1])
            manager.save(passwords,cipher)
            for widget in password_list_frame.winfo_children():
                widget.destroy()
            show_passwords()

    def show_passwords():
        titles()
        i = 1
        for key, value in passwords.items():
            service_labels = ctk.CTkLabel(password_list_frame, text=key)
            service_labels.grid(row=i,column=0,padx=5,pady=2)

            username_labels = ctk.CTkLabel(password_list_frame, text = value["username"])
            username_labels.grid(row=i,column=1,padx=5,pady=2)

            password_labels = ctk.CTkLabel(password_list_frame, text = value["password"])
            password_labels.grid(row=i,column=2,padx=5,pady=2)

            edit_button = ctk.CTkButton(password_list_frame, text = "Edit",width=10, command = lambda r=i: edit(r))
            edit_button.grid(row = i, column = 3, padx=5,pady=2)

            delete_button = ctk.CTkButton(password_list_frame, text = "Delete",width=10, command = lambda r=i: delete(r))
            delete_button.grid(row = i, column = 4, padx=5,pady=2)
            i+=1

    show_passwords()

def login_screen(x):
    clear(x)
    label_button4 = ctk.CTkLabel(x, text = "Login",corner_radius=10, fg_color = "transparent",font = ("Kozuka Gothic Pr6N H",20))
    label_button4.pack(padx=10,pady=10)

    pswd_frame = ctk.CTkFrame(x, corner_radius = 10, height = 120)
    pswd_frame.pack(padx=25,pady=10,fill = "x")

    pswd_label = ctk.CTkLabel(pswd_frame, text = "Enter your password:",corner_radius = 10)
    pswd_label.grid(row = 0,column = 0, padx=10,pady=10)

    login_entry = ctk.CTkEntry(pswd_frame, corner_radius = 10)
    login_entry.grid(column = 1, row = 0, sticky = "e")

    def login():
        if manager.pswd_verification(login_entry.get()) == False:
            feedback_label.configure(text="Wrong Password")
        else:
            feedback_label.configure(text="")
            pswd_manager(x)

    submit_button = ctk.CTkButton(x,text="Submit",corner_radius = 10, command=login)
    submit_button.pack(padx=10,pady=10)
    
    feedback_label = ctk.CTkLabel(x,corner_radius = 10, text = "")
    feedback_label.pack(padx=10,pady=10)
    

def button6(x):
    clear(x)
    if not os.path.exists("system.hash"):
        create_password(x)
    else:
        login_screen(x)
    
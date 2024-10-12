import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.geometry("400x300")
app.title("Bootstrapper")

def show_part_2():
    selected_language = language_list.get()
    selected_version = version_list.get()

    if not selected_language or not selected_version:
        messagebox.showerror("Errr", "Please select both Languege and Version")
        return

    language_label.pack_forget()
    language_list.pack_forget()
    version_label.pack_forget()
    version_list.pack_forget()
    next_button.pack_forget()

    name_label.pack(pady=10)
    name_entry.pack(pady=10)
    server_label.pack(pady=10)
    server_entry.pack(pady=10)
    submit_button.pack(pady=20)

def submit_details():
    user_name = name_entry.get()
    server_name = server_entry.get()

    if not user_name or not server_name:
        messagebox.showerror("Error", "Please fill in all details")
    else:
        messagebox.showinfo("Submitted", f"Name: {user_name}\nServer: {server_name}")

language_label = ctk.CTkLabel(app, text="Select Language")
language_label.pack(pady=10)

language_list = ctk.CTkComboBox(app, values=["Python", "Java"])
language_list.pack(pady=10)

version_label = ctk.CTkLabel(app, text="Select Version")
version_label.pack(pady=10)

version_list = ctk.CTkComboBox(app, values=["Version 1", "Version 2"])
version_list.pack(pady=10)

next_button = ctk.CTkButton(app, text="Next", command=show_part_2)
next_button.pack(pady=20)

name_label = ctk.CTkLabel(app, text="Enter Your Name")
name_entry = ctk.CTkEntry(app)

server_label = ctk.CTkLabel(app, text="Enter Server Name")
server_entry = ctk.CTkEntry(app)

submit_button = ctk.CTkButton(app, text="Submit", command=submit_details)

app.mainloop()

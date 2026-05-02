import tkinter as tk
from tkinter import messagebox
import json
import os
import hashlib
import random
import string
import pyperclip

root = tk.Tk()
root.title("Password Manager")
root.geometry("500x500")
root.configure(bg="#1e1e1e")
is_dark_mode = True

login_label = tk.Label(
    root,
    text="Enter Master Password",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 14)
)

login_label.pack(pady=20)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=10)

def toggle_theme():
    global is_dark_mode

    if is_dark_mode:
        root.configure(bg="white")
        is_dark_mode = False
    else:
        root.configure(bg="#1e1e1e")
        is_dark_mode = True

def open_dashboard():
    # Hide login widgets
    login_label.pack_forget()
    password_entry.pack_forget()
    login_button.pack_forget()

    # Dashboard title
    tk.Label(
        root,
        text="Password Vault Dashboard",
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    tk.Button(
        root,
        text="Toggle Dark/Light Mode",
        command=toggle_theme,
        bg="gray",
        fg="white"
    ).pack(pady=10)

    tk.Label(root, text="Website", bg="#1e1e1e", fg="white").pack()
    website_entry = tk.Entry(root)
    website_entry.pack(pady=5)

    tk.Label(root, text="Username", bg="#1e1e1e", fg="white").pack()
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password", bg="#1e1e1e", fg="white").pack()
    password_vault_entry = tk.Entry(root, show="*")
    password_vault_entry.pack(pady=5)

    def save_credentials():
        website = website_entry.get()
        username = username_entry.get()
        password = password_vault_entry.get()

        if os.path.exists("vault.json"):
         with open("vault.json", "r") as file:
            data = json.load(file)
        else:
            data = {}

        data[website] = {
        "username": username,
        "password": password
        }

        with open("vault.json", "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo("Success", "Credentials Saved!")
    tk.Button(
        root,
        text="Save Password",
        command=save_credentials,
        bg="blue",
        fg="white"
    ).pack(pady=15)

    tk.Label(
        root,
        text="Search Website",
        bg="#1e1e1e",
        fg="white"
    ).pack(pady=10)

    search_entry = tk.Entry(root)
    search_entry.pack(pady=5)

    def retrieve_credentials():
        website = search_entry.get()

        if os.path.exists("vault.json"):
            with open("vault.json", "r") as file:
                data = json.load(file)

            if website in data:
                username = data[website]["username"]
                password = data[website]["password"]

                messagebox.showinfo(
                    "Credentials Found",
                    f"Username: {username}\nPassword: {password}"
                )

            else:
                messagebox.showerror(
                    "Error",
                    "Website not found"
                )

    tk.Button(
        root,
        text="Retrieve Password",
        command=retrieve_credentials,
        bg="purple",
        fg="white"
    ).pack(pady=10) 

    def generate_password():
        length = 12

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        generated_password = ''.join(
            random.choice(characters)
            for i in range(length)
        )

        password_vault_entry.delete(0, tk.END)
        password_vault_entry.insert(0, generated_password)

        pyperclip.copy(generated_password)

        messagebox.showinfo(
            "Success",
            "Password generated and copied to clipboard!"
        )   
    tk.Button(
        root,
        text="Generate Password",
        command=generate_password,
        bg="orange",
        fg="black"
    ).pack(pady=10)

def verify_login():
    entered_password = password_entry.get()

    with open("master.txt", "r") as file:
        saved_password = file.read()

    hashed_entered = hashlib.sha256(
        entered_password.encode()
    ).hexdigest()

    if hashed_entered == saved_password:
        messagebox.showinfo("Success", "Login Successful!")
        open_dashboard()
    else:
        messagebox.showerror("Error", "Wrong Password")

#buttons
login_button = tk.Button(
    root,
    text="Login",
    command=verify_login,
    bg="green",
    fg="white"
)

login_button.pack(pady=20)

root.mainloop()
import os
import json
import hashlib
import base64
import random
import string
import pyperclip
import getpass
import pwinput

def setup_master_password():
    if not os.path.exists("master.txt"):
        print("=== First Time Setup ===")
        
        master_password = pwinput.pwinput(prompt="Create a master password: ", mask="*")
        
        hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
        
        with open("master.txt", "w") as file:
            file.write(hashed_password)
        
        print("Master password created successfully!")

def initialize_vault():
    if not os.path.exists("vault.json"):
        with open("vault.json", "w") as file:
            json.dump({}, file)

def login():
    if os.path.exists("master.txt"):
        with open("master.txt", "r") as file:
            saved_password = file.read()
        
        entered_password = pwinput.pwinput(prompt="Enter Master Password: ", mask="*")
        
        hashed_entered = hashlib.sha256(entered_password.encode()).hexdigest()
        
        if hashed_entered == saved_password:
            print("Login successful!")
            return True
        else:
            print("Wrong password!")
            return False

def add_password():
    website = input("Enter website name: ").strip()
    username = input("Enter username/email: ").strip()
    password = pwinput.pwinput(prompt="Enter password: ", mask="*")
    encrypted_password = encrypt_password(password)

    with open("vault.json", "r") as file:
        data = json.load(file)

    data[website] = {
        "username": username,
        "password": encrypted_password
    }

    with open("vault.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Password saved successfully!")

def retrieve_password():
    website = input("Enter website name to search: ")

    with open("vault.json", "r") as file:
        data = json.load(file)

    if website in data:
        print("\nCredentials Found:")
        print("Username:", data[website]["username"])
        decrypted_password = decrypt_password(data[website]["password"])
        print("Password:", decrypted_password)
    else:
        print("No credentials found for this website.")

def view_websites():
    with open("vault.json", "r") as file:
        data = json.load(file)

    if data:
        print("\nSaved Websites:")
        for website in data:
            print("-", website)
    else:
        print("No passwords saved yet.")

def encrypt_password(password):
    encoded = base64.b64encode(password.encode()).decode()
    return encoded

def decrypt_password(encoded_password):
    decoded = base64.b64decode(encoded_password.encode()).decode()
    return decoded

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for i in range(length))
    print("Generated Password:", generated_password)
    pyperclip.copy(generated_password)
    print("Password copied to clipboard successfully!")

setup_master_password()
initialize_vault()

if login():
    while True:
        print("\n--- Password Manager Menu ---")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. View Saved Websites")
        print("4. Generate Password")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password()

        elif choice == "2":
            retrieve_password()

        elif choice == "3":
            view_websites()

        elif choice == "4":
            generate_password()

        elif choice == "5":
            print("Exiting Password Manager...")
            break

        else:
            print("Invalid choice!")


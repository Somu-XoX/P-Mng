# P-Mng 🔐

A Python-based GUI Password Manager built using Tkinter.

This application allows users to securely store and retrieve website credentials using a master password login system.

---

## Features

- Master Password Authentication
- Save Website Credentials
- Retrieve Saved Credentials
- Random Password Generator
- Auto Copy Generated Password to Clipboard
- Dark/Light Mode Toggle
- Local JSON Storage

---

## Tech Stack

- Python
- Tkinter
- JSON
- Hashlib
- Random
- String
- Pyperclip

---

## Requirements

Before running this project, make sure you have:

### 1. Python Installed
Download Python from:

: winget install Python.Python.3   (Run in Command Prompt with admin permission)

Recommended version:

```bash
Python 3.10+
```

Check installation:

```bash
python --version
```

---

### 2. Install Required Module

This project uses one external module:

```bash
pip install pyperclip
```

Tkinter usually comes pre-installed with Python.

If not:

For Ubuntu/Linux:

```bash
sudo apt-get install python3-tk
```

---

## Project Files

```bash
SecureVault/
│
├── gui.py
├── README.md
├── .gitignore
```

Generated automatically while using app:

```bash
master.txt
vault.json
```

---

## How to Run This Project on Another PC

### Step 1: Clone Repository

```bash
git clone https://github.com/Somu-XoX/P-Mng.git
```

Replace with your actual GitHub repo link.

---

### Step 2: Open Project Folder

```bash
cd SecureVault
```

---

### Step 3: Install Dependencies

```bash
pip install pyperclip
```

---

### Step 4: Run Application

```bash
python gui.py
```

---

## How to Use

### First Time Use
- Run the application
- Create a master password
- Login using that password

---

### Save Credentials
- Enter website name
- Enter username/email
- Enter password
- Click **Save Password**

---

### Retrieve Credentials
- Enter website name in search box
- Click **Retrieve Password**

---

### Generate Password
- Click **Generate Password**
- Password will:
  - Auto-fill password field
  - Copy automatically to clipboard

---

### Theme Toggle
- Click **Toggle Dark/Light Mode**

---

## Future Improvements

- Real Encryption using Cryptography
- Cloud Sync
- Mobile App Version
- Web App Version

---

## Author

Built by Somu 🚀

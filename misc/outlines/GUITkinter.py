import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
import random

class DataManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Dorian's Data System")

        # Variables for user input
        self.domain_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Variables for Generate Password frame
        self.amount_var = tk.StringVar()
        self.length_var = tk.StringVar()
        self.special_var = tk.StringVar()
        self.numbers_var = tk.StringVar()
        self.lowercase_var = tk.StringVar()
        self.capitals_var = tk.StringVar()

        # Existing saved data
        self.saved_logins = {}
        self.saved_address = {}
        self.saved_banking_info = {}
        self.saved_ssn = {}

        # Load saved data from file
        self.load_data_from_file()

        # Create a single frame for content
        self.content_frame = ttk.Frame(self.root, style='TFrame')
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2C3E50')  # Blackish-gray background
        self.style.configure('TLabel', background='#2C3E50', foreground='white', font=('Helvetica', 14, 'bold'))
        self.style.configure('TEntry', background='#B74343', font=('Arial', 12), foreground='black', padding=10)
        self.style.configure('TButton', background='#B74343', foreground='black', font=('Helvetica', 14, 'bold'))

        # Initial content to show
        self.show_main_menu()

    def load_data_from_file(self):
        DATA_FILE = 'save_data.json'
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                saved_data = json.load(file)
                self.saved_logins = saved_data.get('logins', {})
                self.saved_address = saved_data.get('address', {})
                self.saved_banking_info = saved_data.get('banking_info', {})

    def save_data_to_file(self):
        DATA_FILE = 'save_data.json'
        data_to_save = {
            'logins': self.saved_logins,
            'address': self.saved_address,
            'banking_info': self.saved_banking_info
        }
        with open(DATA_FILE, 'w') as file:
            json.dump(data_to_save, file)

    def show_main_menu(self):
        # Clear existing content
        self.clear_content()

        # Show Main Menu
        ttk.Label(self.content_frame, text="Select an option:", style='TLabel').pack(pady=20)

        # Buttons for different options
        options = ['Save Login', 'Generate Password', 'Save Personal Information', 'Save Banking Info', 'See All Saved Data']
        for option in options:
            ttk.Button(self.content_frame, text=option, command=lambda o=option: self.show_content(o), style='TButton').pack(pady=15)

    def show_content(self, option):
        # Clear existing content
        self.clear_content()

        # Add a back button
        ttk.Button(self.content_frame, text="Back", command=self.show_main_menu, style='TButton').pack(pady=20)

        if option == 'Save Login':
            self.show_save_login_content()
        elif option == 'Generate Password':
            self.show_generate_password_content()
        elif option == 'Save Personal Information':
            self.show_personal_information_content()
        elif option == 'Save Banking Info':
            self.show_banking_info_content()
        elif option == 'See All Saved Data':
            self.show_see_all_data_content()

    def show_save_login_content(self):
        # Show Save Login content
        ttk.Label(self.content_frame, text="Domain:", style='TLabel').pack(pady=10)
        ttk.Entry(self.content_frame, textvariable=self.domain_var, style='TEntry').pack(pady=5)
        ttk.Label(self.content_frame, text="Username/Email:", style='TLabel').pack(pady=10)
        ttk.Entry(self.content_frame, textvariable=self.username_var, style='TEntry').pack(pady=5)
        ttk.Label(self.content_frame, text="Password:", style='TLabel').pack(pady=10)
        ttk.Button(self.content_frame, text="Enter Password", command=self.enter_password, style='TButton').pack(pady=20)
        ttk.Button(self.content_frame, text="Save Login", command=self.save_login, style='TButton').pack(pady=30)

    def show_generate_password_content(self):
        # Show Generate Password content
        ttk.Label(self.content_frame, text="Amount of passwords:", style='TLabel').pack(pady=10)
        ttk.Entry(self.content_frame, textvariable=self.amount_var, style='TEntry').pack(pady=5)
        ttk.Label(self.content_frame, text="Length of password:", style='TLabel').pack(pady=10)
        ttk.Entry(self.content_frame, textvariable=self.length_var, style='TEntry').pack(pady=5)
        ttk.Label(self.content_frame, text="Special characters to exclude:", style='TLabel').pack(pady=10)
        ttk.Entry(self.content_frame, textvariable=self.special_var, style='TEntry').pack(pady=5)
        ttk.Label(self.content_frame, text="Numbers to exclude:", style='TLabel').pack(pady=10)
        ttk.Entry(self.content_frame, textvariable=self.numbers_var, style='TEntry').pack(pady=5)
        ttk.Label(self.content_frame, text="Lowercase letters to exclude:", style='TLabel').pack(pady=10)
        ttk.Entry(self.content_frame, textvariable=self.lowercase_var, style='TEntry').pack(pady=5)
        ttk.Label(self.content_frame, text="Capital letters to exclude:", style='TLabel').pack(pady=10)

        self.result_text = tk.Text(self.content_frame, height=5, width=30, wrap=tk.WORD, font=('Arial', 12), bg='#B74343', fg='black')
        self.result_text.pack(pady=20)
        ttk.Button(self.content_frame, text="Generate Password", command=self.generate_passwords, style='TButton').pack(pady=30)

    def enter_password(self):
        password = simpledialog.askstring("Password Entry", "Enter Password:", show='*')
        self.password_var.set(password)

    def show_personal_information_content(self):
        # Your existing personal information code goes here
        pass

    def show_banking_info_content(self):
        # Your existing banking info code goes here
        pass

    def show_see_all_data_content(self):
        # Your existing see all data code goes here
        pass

    def save_login(self):
        domain = self.domain_var.get()
        username = self.username_var.get()
        password = self.password_var.get()

        # Your existing code to save login information
        self.saved_logins[domain] = {'Username': username, 'Password': password}

        # Inform the user
        messagebox.showinfo("Saved", "Login information saved successfully.")

        # Save data to file
        self.save_data_to_file()

        # Go back to the initial content
        self.show_main_menu()

    def clear_content(self):
        # Destroy all widgets in the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def generate_passwords(self):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%^&*()_+-=[]{}|;:,.<>/?~'
        number = int(self.amount_var.get())
        length = int(self.length_var.get())
        special = self.special_var.get()
        numbers = self.numbers_var.get()
        lowercase = self.lowercase_var.get()
        capitals = self.capitals_var.get()

        passwords = []

        for _ in range(number):
            password = ''
            for _ in range(length):
                char = random.choice(chars)
                if char not in special and char not in numbers and char not in lowercase and char not in capitals:
                    password += char
            passwords.append(password)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "\n".join(passwords))

if __name__ == "__main__":
    root = tk.Tk()
    app = DataManagementSystem(root)
    root.geometry("800x600")
    root.mainloop()

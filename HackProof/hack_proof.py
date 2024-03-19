import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string
import random
class HackProof():
    def __init__(self, root):
        self.root = root
        self.root.title("Hack Proof")
        self.root.geometry("320x200")

        self.label = ttk.Label(root, text="Create Username and Password")
        self.label.grid(row=0, column=0, columnspan=6, pady=5)
        
        # username
        self.username_label = ttk.Label(root, text="Username:")
        self.username_label.grid(row=1, column=0, sticky='w')
        self.username_entry = ttk.Entry(root)
        self.username_entry.grid(row=1, column=1)
        
        # password 
        self.password_label = ttk.Label(root, text="Password:")
        self.password_label.grid(row=2, column=0, sticky='w')
        self.password_entry = ttk.Entry(root, show="*")
        self.password_entry.grid(row=2, column=1)
        
        # create random passowrd button
        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=2, padx=10)

        # create save login button
        self.save_button = ttk.Button(root, text="Save", command=self.save_details)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_password(self):
        # define character set for password
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password =  ''.join(random.choice(characters) for _ in range(8))
        response = messagebox.askyesno("Random Password", f"Do you want to use the generated password?\nPassword: {password}")
        if response:
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
    
    def save_details(self):
        pass

    def verify_password(self):
        pass

root = tk.Tk()

hack_proof = HackProof(root)

root.mainloop()
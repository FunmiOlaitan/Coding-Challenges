import tkinter as tk
from tkinter import ttk

class HackProof():
    def __init__(self, root):
        self.root = root
        self.root.title("Hack Proof")
        self.root.geometry("200x300")

        self.label = ttk.Label(root, text="Create Username and Password")
        self.label.grid(row=0, column=0, columnspan=6)

        self.username_label = ttk.Label(root, text="Username:")
        self.username_label.grid(row=2, column=0, sticky='w')
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=2, column=1)

        self.password_label = ttk.Label(root, text="Password:")
        self.password_label.grid(row=3, column=0, sticky='w')
        self.password_entry = ttk.Entry(root)
        self.password_entry.grid(row=3, column=1)


root = tk.Tk()

hack_proof = HackProof(root)

root.mainloop()
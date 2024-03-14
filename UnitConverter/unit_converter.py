import tkinter as tk
from tkinter import ttk

class UnitConverterApp:
    def _init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("300x100")

        # Variables to store user selections
        self.category_var = tk.StringVar()

        # Frame for screen 1
        self.screen1_frame = ttk.Frame(root)
        self.screen1_frame.pack()

        ttk.Label(self.screen1_frame, text="Select Category:").pack()
        self.category_dropdown = ttk.Combobox(self.screen1_frame, textvariable=self.category_var, values=["Length", "Temperature", "Volume", "Area"])
        self.category_dropdown.pack()
        ttk.Button(self.screen1_frame, text="Next").pack()
        
        # Frame for screen 2
        self.screen2_frame = ttk.Frame(root)

    def show_screen2(self):
        pass
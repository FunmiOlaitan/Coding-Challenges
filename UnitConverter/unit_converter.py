import tkinter as tk
from tkinter import ttk

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("300x100")

        # Variables to store user selections
        self.category_var = tk.StringVar()

        # Frame for screen 1
        self.screen1_frame = ttk.Frame(root)
        self.screen1_frame.pack()

        # Label and dropdown for selecting category
        ttk.Label(self.screen1_frame, text="Select Category:").pack()
        self.category_dropdown = ttk.Combobox(self.screen1_frame, textvariable=self.category_var, values=["Length", "Temperature", "Volume", "Area"])
        self.category_dropdown.pack()
        ttk.Button(self.screen1_frame, text="Next", command=self.show_screen2).pack()
        
        # Frame for screen 2
        self.screen2_frame = ttk.Frame(root)

    def show_screen2(self):
        # Hide screen 1 and show screen 2
        self.screen1_frame.pack_forget()
        self.screen2_frame.pack()
        pass

# Create the root window
root = tk.Tk()
# Create an instance of UnitConverter
converter = UnitConverterApp(root)
# Start the Tkinter event loop
root.mainloop()
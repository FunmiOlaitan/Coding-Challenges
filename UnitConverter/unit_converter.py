import tkinter as tk
from tkinter import ttk

class UnitConverterApp:
    def __init__(self, root):
        # Main window setup 
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("300x200")

        # Variables to store user selections
        self.category_var = tk.StringVar() # (eg.Length, Temp)
        self.unit_from_var = tk.StringVar() # (e.g., Meter to Kilometer) 
        self.unit_to_var = tk.StringVar()
        self.value_var = tk.StringVar()

        # Frame for screen 1
        self.screen1_frame = ttk.Frame(root)  # A container (frame) that holds all the widgets for the first screen
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
        
        # Create widgets for screen 2 based on selected category
        category = self.category_var.get()

        if category == "Length":
            units = ["Meter (m)", "Kilometer (km)", "Centimeter (cm)"]
        elif category == "Temperature":
            units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
        elif category == "Volume":
            units = ["Liter (L)", "Milliliter (mL)", "Cubic Meter (m³)"]
        elif category == "Area":
            units = ["Square Meter (m²)", "Square Kilometer (km²)", "Square Centimeter (cm²)"]
        
        # Labels and dropdowns for selecting units
        ttk.Label(self.screen2_frame, text="Convert from:").pack()
        self.unit_from_dropdown = ttk.Combobox(self.screen2_frame, textvariable=self.unit_from_var, values=units)
        self.unit_from_dropdown.pack()
        ttk.Label(self.screen2_frame, text="Convert to:").pack()
        self.unit_to_dropdown = ttk.Combobox(self.screen2_frame, textvariable=self.unit_to_var, values=units)
        self.unit_to_dropdown.pack(pady=(0,20))

        # Entry widget to input value to convert
        ttk.Label(self.screen2_frame, text="Enter value to convert:").pack()
        self.value_entry = ttk.Entry(self.screen2_frame, textvariable=self.value_var)  # Entry widget for input value
        self.value_entry.pack()

        
root = tk.Tk()
converter = UnitConverterApp(root)
# Start the Tkinter event loop
root.mainloop()
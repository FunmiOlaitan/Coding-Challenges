import tkinter as tk
from tkinter import messagebox


class LengthCalculator:
    def __init__(self):
        # Initialise units in length 
        self.m_conversions = {
            "km": 0.001,
            "cm": 100
        }
        self.km_conversions = {
            "cm": 100000,
            "m": 1000
        }
        self.cm_conversions = {
            "m": 0.01,
            "km": 0.00001
        }
    def meter_conversion(self):
        pass

    def centimeter_conversion(self):
        pass
    def kilometer_conversion(self):
        pass

class TemperatureCalculator:
    pass

class VolumeCalculator:
    pass

class AreaCalculator:
    pass

# Create tkinter window 
root = tk.Tk()
root.title("Unit_converter")

label = tk.Label(root, text="Welcome to Unit Converter")


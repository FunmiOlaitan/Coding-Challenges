import csv
import random 
from datetime import datetime, time
import re

class TestDataGenerator:
    def __init__(self, num_rows, field_names, csv_file):
        self.num_rows = num_rows
        self.field_names = field_names
        self.csv_file = csv_file
    
    def random_car_type(self):
        return random.choice(['BMW','Toyota','Honda','Ford','Audi','Volkswagen','Hyundai','Nissan', 'Mercedes-Benz'])
    
    def random_number_plate(self):
        if random.random() < 0.8:
            letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
            numbers = ''.join(random.choices('0123456789', k=2))
            numbers_after = ''.join(random.choices('0123456789', k=3))
            return f"{letters}{numbers} {numbers_after}"
        else:
            return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=7))
   
    def random_time(self, start_hour, end_hour):
        hour = random.randint(start_hour, end_hour)
        minute = random.randint(0, 29)
        second = random.randint(0, 59)
        return time(hour, minute, second)
    
    def generate_data(self, start_hour, end_hour):
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.field_names)
            writer.writeheader()
            for _ in range(self.num_rows):
                # Generate random data for each row
                writer.writerow({
                    'Car': self.random_car_type(),
                    'Plate': self.random_number_plate(),
                    'camera1_time':  self.random_time(start_hour, end_hour).strftime("%H:%M:%S"),
                    'camera2_time':  self.random_time(start_hour, end_hour).strftime("%H:%M:%S")
                })
        print(f"Data has been generated and saved to {self.csv_file}.")

class ValidNumberPlate:
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    def validate_number_plate(self, plate):
        pattern = re.compile(r'^[A-Z]{2}\d{2}\s\d{3}$')
        return bool(pattern.match(plate))
    
    def update_csv(self):
        rows = []
        fieldnames = None
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames + ['Valid']
            for row in reader:
                plate = row['Plate']
                is_valid = self.validate_number_plate(plate)
                row['Valid'] = 'Yes' if is_valid else 'No'
                rows.append(row)
          
        # Write updated rows back to CSV
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Validation completed. Updated CSV: {self.csv_file}")

class Speeding:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def calculate_speed_and_violators(self, speed_limit, distance_miles):
        violators = []
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                plate = row['Plate']
                camera1_time = datetime.strptime(row['camera1_time'], "%H:%M:%S")
                camera2_time = datetime.strptime(row['camera2_time'], "%H:%M:%S")
                time_difference = camera2_time - camera1_time
                time_difference_hours = time_difference.total_seconds() / 3600
                average_speed_mph = distance_miles / time_difference_hours
                if average_speed_mph > speed_limit:
                    violators.append((plate, average_speed_mph))
        return violators 
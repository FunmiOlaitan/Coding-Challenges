import csv
import random
from datetime import datetime, time, timedelta
import re
import os

class TestDataGenerator:
    def __init__(self, num_rows, field_names, folder_name):
        """
        Initializes the test data generator.
        """
        self.num_rows = num_rows
        self.field_names = field_names
        self.folder_name = folder_name
    
    def random_car_type(self):
        """
        Returns a random car type from a predefined list.
        """
        return random.choice(['BMW', 'Toyota', 'Honda', 'Ford', 'Audi', 'Volkswagen', 'Hyundai', 'Nissan', 'Mercedes-Benz'])
    
    def random_number_plate(self):
        """
        Returns a random number plate.
        """
        if random.random() < 0.8:
            letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
            numbers = ''.join(random.choices('0123456789', k=2))
            numbers_after = ''.join(random.choices('0123456789', k=3))
            return f"{letters}{numbers} {numbers_after}"
        else:
            return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=7))
   
    def random_time(self, start_hour, end_hour):
        """
        Returns a random time within the specified hour range.
        """
        hour = random.randint(start_hour, end_hour)
        minute = random.randint(0, 29)
        second = random.randint(0, 59)
        return time(hour, minute, second)
    
    def generate_data(self, start_hour, end_hour):
        """
        Generates random test data and writes it to a CSV file.
        """
        os.makedirs(self.folder_name, exist_ok=True)
        csv_file_path = os.path.join(self.folder_name, 'data.csv')

        try:
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.field_names)
                writer.writeheader()
                for _ in range(self.num_rows):
                    camera1_time = self.random_time(start_hour, end_hour)
                    min_time_diff = timedelta(minutes=1)  # Minimum realistic time difference
                    max_time_diff = timedelta(minutes=30)  # Maximum realistic time difference
                    random_diff = random.uniform(min_time_diff.total_seconds(), max_time_diff.total_seconds())
                    camera2_time = (datetime.combine(datetime.today(), camera1_time) + timedelta(seconds=random_diff)).time()
                    
                    writer.writerow({
                        'Car': self.random_car_type(),
                        'Plate': self.random_number_plate(),
                        'camera1_time': camera1_time.strftime("%H:%M:%S"),
                        'camera2_time': camera2_time.strftime("%H:%M:%S")
                    })
            print(f"Data has been generated and saved to {csv_file_path}.")
        except Exception as e:
            print(f"An error occurred while writing to the CSV file: {e}")

class ValidNumberPlate:
    def __init__(self, csv_file_path):
        """
        Initializes the number plate validator.
        """
        self.csv_file_path = csv_file_path
    
    def validate_number_plate(self, plate):
        """
        Validates a number plate against a regex pattern.
        """
        pattern = re.compile(r'^[A-Z]{2}\d{2}\s\d{3}$')
        return bool(pattern.match(plate))
    
    def update_csv(self):
        """
        Updates the CSV file with validation results for each number plate.
        """
        rows = []
        try:
            with open(self.csv_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames + ['Valid']
                for row in reader:
                    plate = row['Plate']
                    is_valid = self.validate_number_plate(plate)
                    row['Valid'] = 'Yes' if is_valid else 'No'
                    rows.append(row)
            
            with open(self.csv_file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            print(f"Validation completed. Updated CSV: {self.csv_file_path}")
        except Exception as e:
            print(f"An error occurred while updating the CSV file: {e}")

class Speeding:
    def __init__(self, csv_file_path):
        """
        Initializes the speeding checker.
        """
        self.csv_file_path = csv_file_path

    def calculate_speed_and_violators(self, speed_limit, distance_miles):
        """
        Calculates the speed of cars and identifies violators.
        """
        violators = []
        try:
            with open(self.csv_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    plate = row['Plate']
                    camera1_time = datetime.strptime(row['camera1_time'], "%H:%M:%S")
                    camera2_time = datetime.strptime(row['camera2_time'], "%H:%M:%S")
                    if camera2_time < camera1_time:
                        camera2_time += timedelta(days=1)
                    time_difference = camera2_time - camera1_time
                    time_difference_hours = time_difference.total_seconds() / 3600
                    average_speed_mph = distance_miles / time_difference_hours
                    if average_speed_mph > speed_limit:
                        violators.append((plate, average_speed_mph))
            return violators 
        except Exception as e:
            print(f"An error occurred while calculating speeds: {e}")
            return violators

def main():
    """
    Main function to generate data, validate number plates, and check for speeding violations.
    """
    # Test the data generator
    field_names = ['Car', 'Plate', 'camera1_time', 'camera2_time']
    folder_name = 'SpeedTracker'
    num_rows = 100
    data_generator = TestDataGenerator(num_rows, field_names, folder_name)
    data_generator.generate_data(8, 20)

    # Construct the full path for the CSV file
    csv_file_path = os.path.join(folder_name, 'data.csv')

    # Validate number plates
    validator = ValidNumberPlate(csv_file_path)
    validator.update_csv()

    # Check for speeding violations
    speed_checker = Speeding(csv_file_path)
    speed_limit = 60  # in mph
    distance_miles = 50  # distance between cameras in miles
    violators = speed_checker.calculate_speed_and_violators(speed_limit, distance_miles)
    print("Speeding Violators:")
    for violator in violators:
        print(f"Plate: {violator[0]}, Average Speed: {violator[1]} mph")

if __name__ == "__main__":
    main()

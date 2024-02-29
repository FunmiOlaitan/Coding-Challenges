import csv
import random 
import datetime

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
            numbers_after =''.join(random.choices('0123456789', k= 3))
            return f"{letters}{numbers} {numbers_after}"
        else:
            return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=7))
        
    def random_time_before(self):
        hour = 3
        minute = random.randit(0, 29)
        second = random.randit(0, 59)
        time = datetime.time(hour,minute,second)
        return time.strftime("%H:%M:%S")
    
    def random_time_after(self):
        hour = 3
        minute = random.randit(30, 59)
        second = random.randit(0, 59)
        time = datetime.time(minute,hour,second)
        return time.strftime("%H:%M:%S")

    def generate_data(self):
        with open(self.csv_file, mode='w', newline= '') as file:
            writer = csv.DictWriter(file, feildnames=self.field_names)
            writer.writeheader()
            for _ in range(self.num_rows):
                # Generate random data for each row
                writer.writerow({
                    'Car': self.random_car_type(),
                    'Plate': self.random_number_plate(),
                    'TimeFirstCamera': self.random_time_before(),
                    'TimeSecondCamera': self.random_time_after()
                })
        print(f"Data has been generated and saved to {self.csv_file}.")    

class ValidNumberPlate:
    pass

class Speeding:
    pass
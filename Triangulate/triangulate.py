import math
class Triangulate:
    def __init__(self):
        self.first_side = None
        self.second_side = None
        self.third_side = None
    
    def get_dimensions(self):
        print("Please enter the length for all three sides of your triangle")
        while True:
            try:
                self.first_side = float(input("Length of the first side: "))
                self.second_side = float(input("Length of the second side: "))
                self.third_side = float(input("Length of the third side: "))
                if self.first_side <= 0 or self.second_side <= 0 or self.third_side <=0:
                    print("Length must be positive numbers. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter numerical values")
    
    def validate_triangle(self):
        # Assign side lengths to temporary variables
        a = self.first_side
        b = self.second_side
        c = self.third_side
        
        # If all three conditions are met, then the sides can form a valid triangle.
        if a + b > c and a + c > b and b + c > a:
            # If all conditions are met, return True (valid triangle)
            return True 
        else:
            return False 
        
    def classify_triangle(self):
        a = self.first_side
        b = self.second_side
        c = self.third_side
        
        if a == b and a == c:
            return "This is a Equilateral triangle"
        elif a != b and a != c and b != c:
            return "This is a Scalene triangle"
        elif a == b or a == c or b == c:
            return "This is a Isosceles triangle"
        elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return "This is a Right-Angle triangle"
        else:
            return None

    def calculate_missing_side(self, angle, side_one, side_two):
        # Convert angle from degrees to radians
        angle_in_radians = math.radians(angle)

        # Use the sine rule to calculate the missing side length
        missing_length = math.sin(angle_in_radians) * (side_two / math.sin(math.pi - angle_in_radians))

        print(f"The length of the missing side is: {missing_length}")

    def main(self):
        # Get triangle dimensions
        self.get_dimensions()

        # Check if the triangle is valid
        is_valid_triangle = self.validate_triangle()

        if is_valid_triangle:
            print(f"With lengths: {self.first_side}, {self.second_side}, {self.third_side}")

            # Classify the triangle
            triangle_type = self.classify_triangle()
            print(triangle_type)
        # Check if the triangle is not equilateral (since all sides are equal)
            if triangle_type != "This is a Equilateral triangle":
                print("To calculate missing side:")
                angle = float(input("Please enter the angle in degrees: "))
                side_one = float(input("Please enter the length of the first side: "))
                side_two = float(input("Please enter the length of the second side: "))
                self.calculate_missing_side(angle, side_one, side_two)
        else:
            print("This is not a valid triangle")

triangle_calculator = Triangulate()
triangle_calculator.main()
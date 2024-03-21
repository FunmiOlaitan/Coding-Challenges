class Triangulate:
    def __init__(self):
        self.first_side = None
        self.second_side = None
        self.third_side = None
    
    def get_dimensions(self):
        print("Please enter the length for all three sides of a triangle:")
        while True:
            try:
                self.first_side = float(input("Please enter the length of the first side if the triangle: "))
                self.second_side = float(input("Please enter the length of the second side of the triangle: "))
                self.third_side = float(input("Please enter the length of the third side of the triangle: "))
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
        pass

    def calculate_missing_side(self, angle):
        pass
import math

class Triangle:
    def __init__(self):
        self.sides = []

    def get_dimensions(self):
        print("Please enter the lengths of the three sides of your triangle:")
        while True:
            try:
                self.sides = [float(input(f"Length of side {i + 1}: ")) for i in range(3)]
                if any(side <= 0 for side in self.sides):
                    print("Lengths must be positive numbers. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter numerical values.")

    def validate_triangle(self):
        a, b, c = sorted(self.sides)
        if a + b > c:
            return True
        print("This is not a valid triangle.")
        return False

    def classify_triangle(self):
        a, b, c = sorted(self.sides)
        if a == b == c:
            return "This is an Equilateral triangle."
        elif a == b or b == c or a == c:
            if math.isclose(a**2 + b**2, c**2, rel_tol=1e-9):
                return "This is an Isosceles Right-Angle triangle."
            return "This is an Isosceles triangle."
        elif math.isclose(a**2 + b**2, c**2, rel_tol=1e-9):
            return "This is a Right-Angle triangle."
        else:
            return "This is a Scalene triangle."

    def calculate_side_using_law_of_cosines(self, angle, side_one, side_two):
        angle_in_radians = math.radians(angle)
        missing_length = math.sqrt(side_one**2 + side_two**2 - 2 * side_one * side_two * math.cos(angle_in_radians))
        print(f"The length of the missing side is: {missing_length:.2f}")

    def additional_calculations(self):
        try:
            angle = float(input("Please enter the angle in degrees: "))
            side_one = float(input("Please enter the length of the first side: "))
            side_two = float(input("Please enter the length of the second side: "))
            if angle <= 0 or side_one <= 0 or side_two <= 0:
                print("All inputs must be positive numbers.")
            else:
                self.calculate_side_using_law_of_cosines(angle, side_one, side_two)
        except ValueError:
            print("Invalid input. Please enter numerical values.")

    def main(self):
        self.get_dimensions()
        if self.validate_triangle():
            print(f"With lengths: {self.sides}")
            triangle_type = self.classify_triangle()
            print(triangle_type)
            if triangle_type != "This is an Equilateral triangle.":
                self.additional_calculations()

if __name__ == "__main__":
    triangle_calculator = Triangle()
    triangle_calculator.main()

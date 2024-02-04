def generate_pin_combinations(digits):
    def permute(prefix, remaining):
        if not remaining:
            combinations.append(prefix)
            return
        for i in range(len(remaining)):
            new_prefix = prefix + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            permute(new_prefix, new_remaining)

    # Initialize combinations list
    combinations = []

    # Start recursion
    permute('', digits)

    # Display result
    return combinations

def main():
# Take user input: Prompt the user to enter four numerical digits.
    while True:
        code = input("Enter a four-digit number: ")
    
        if len(code) == 4 and code.isdigit():
            print("Code valid")
            break   
        else:
            print("\nInput is invalid. Please enter a four-digit number.") 

    # Generate combinations
    pin_combinations = generate_pin_combinations(code)

    # Display the combinations
    print("\nAll possible combinations")
    for combination in pin_combinations:
        print(combination)
    
if __name__ == "__main__":
    main()

# Take user input: Prompt the user to enter four numerical digits.
while True:
    code = input("Enter a four-digit number: ")
    
    if len(code) == 4 and code.isdigit():
        print("Code valid")
        break   
    else:
        print("\nInput is invalid. Please enter a four-digit number.") 


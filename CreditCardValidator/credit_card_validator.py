def validate_luhn_algo(credit_card_number):
    card_number = ''.join(char for char in credit_card_number if char.isdigit())
    # converts each digit in the string into a int and store in list 
    digits = [int(num) for num in card_number]
    checksum = 0

    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    checksum = sum(digits) % 10
    return checksum == 0

def validate_credit_card_length(credit_card_number):
    card_number = ''.join(char for char in credit_card_number if char.isdigit())

    card_length = len(card_number)
    if 13 <= card_length <= 16:
        return True 
    else:
        return False 
    
def validate_credit_card_vendor(credit_card_number):
    # This line of code removes any non-digit characters before checking vendor
    card_number =  ''.join(char for char in credit_card_number if char.isdigit())

    if card_number.startswith('34') or card_number.startswith ('37'):
        return "American Express"
    elif 51 <= int(card_number[:2]) <= 55:
        return "Mastercard"
    elif card_number.startswith('4'):
        return "Visa"
    elif card_number.startswith('6011'):
        return "Discover"
    else:
        return None

def main():
    credit_card_number = input("Enter credit card number: ")

    if not validate_credit_card_length(credit_card_number):
        print("Invalid credit card number length.")
        return

    vendor = validate_credit_card_vendor(credit_card_number)
    if vendor:
        print("Credit card vendor:", vendor)
    else:
        print("Unknown credit card vendor.")
        return

    if validate_luhn_algo(credit_card_number):
        print("Valid credit card number.")
    else:
        print("Invalid credit card number.")

if __name__ == "__main__":
    main()
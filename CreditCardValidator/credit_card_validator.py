def luhn_algo(number):
    # converts each digit in the string into a int and store in list 
    digits = []

    for num in number:
        digit = int(num)
        digits.append(digit)
    
    checksum = 0

    for i in range(len(digits) -2, -1, -2):
        digits[i] *=2
        if digits[i] > 9:
            digits[i] -=9
    
    checksum = sum(digits) % 10
    return checksum == 0

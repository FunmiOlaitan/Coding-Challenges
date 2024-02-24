# Credit Card Validator 

This Python script validates credit card numbers using the Luhn algorithm and checks their length and vendor.

## Features

- **Luhn Algorithm Validation**: Validates credit card numbers using the Luhn algorithm.
- **Length Validation**: Checks if the length of the credit card number is within the valid range (13-16 digits).
- **Vendor Identification**: Identifies the vendor of the credit card (e.g., American Express, Mastercard, Visa, Discover).

## Usage

1. Run the script.
2. Enter the credit card number when prompted.

## Running the Script

To run the script, execute the following command in your terminal:

```
python credit_card_validator.py
```

## Example

```
Enter credit card number: 4242424242424242
Credit card vendor: Visa
Valid credit card number.
```

```
Enter credit card number: 378282246310005
Credit card vendor: American Express
Valid credit card number.
```

```
Enter credit card number: 1234567890123456
Unknown credit card vendor.
Invalid credit card number length.
```

## Note

- Ensure you input only the digits of the credit card number without any spaces or special characters.

## Contact

If you have any questions or suggestions regarding the coding challenges, feel free to contact me at [FunmilolaOlaitan@yahoo.com].


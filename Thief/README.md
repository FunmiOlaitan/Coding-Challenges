# Thief! - PIN Code Combination Finder

## Overview

Thief! is a simple command-line program designed to help a thief find the correct sequence for an online PIN code. The thief has successfully obtained the four digits of the PIN but needs to determine the correct order to access the targeted account. This program generates and displays all possible combinations for the provided four numerical digits, ensuring that each combination is unique.

## Features

- User-friendly command-line interface.
- Generates and displays all possible combinations for a given set of four numerical digits.
- Avoids displaying duplicate combinations to streamline the hacking process.

## Getting Started

### Prerequisites

- Make sure you have a compatible programming environment installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/FunmiOlaitan/Coding-Challenges.git
   ```

2. Navigate to the project directory:

   ```bash
   cd thief
   ```

3. Run the program:

   ```bash
   python thief.py
   ```

## Usage

1. Launch the program by running the above command.
2. Enter the four numerical digits obtained by the thief when prompted.
3. The program will display all possible unique combinations for the entered digits.

## Showcase

### Sample Run

```bash
$ python thief.py

Welcome to Thief! - PIN Code Combination Finder

Enter the four numerical digits (e.g., 1234): 9876

Generating combinations...

Unique Combinations:
1. 9876
2. 9768
3. 9678
4. 9687
5. 9786
6. 9765
7. 9675
8. 9685
9. 9785
10. 9756
11. 9657
12. 9658
13. 9758
14. 9857
15. 9856
```

### Notes

- The program ensures that each combination is unique.
- The generated combinations can be used by the thief to attempt access to the targeted account.

## Contact

If you have any questions or suggestions regarding the coding challenges, feel free to contact me at [FunmilolaOlaitan@yahoo.com].

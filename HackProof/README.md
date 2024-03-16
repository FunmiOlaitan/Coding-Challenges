# Hack-Proof Text Document Access Program

**Description:**
This program is designed to provide access to a text document only if the correct username and password are entered. It includes features such as generating suggested passwords and verifying password strength according to specific criteria.

**Features:**
1. **Username and Password Creation:** Users can create a username and password to access the text document.
2. **Random Password Generation:**
   - Extension 1: Generates a random password of at least 8 characters as a suggested password.
   - Extension 2: Generates a random password that contains at least one lowercase letter, one uppercase letter, and one special character, with a minimum length of 8 characters.
3. **Password Verification:**
   - Verifies that the password provided by the user meets the criteria set in the extensions mentioned above.
   - Checks if the password matches the suggested password generated in Extension 1.
   - Ensures that the password meets specific criteria mentioned in Extension 2.
4. **Graphical User Interface (GUI):**
   - Utilizes tkinter library for creating a user-friendly interface.

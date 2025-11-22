title: "Random Password Generator"
author: "Sharangan Nedunchelian"
description: "A Python-based GUI password generator with difficulty selection, strength calculation, and clipboard copy functionality."

overview: |
  This is a Python-based password generator with a graphical interface built using Tkinter. 
  It allows users to generate passwords of varying difficulty levels and evaluates their strength. 
  Users can also copy the generated password to the clipboard with one click.

features:
  - Generate passwords of Easy, Medium, or Hard difficulty
  - Supports letters, digits, and punctuation
  - Password strength calculation based on:
      - Length of the password
      - Character types included (lowercase, uppercase, digits, punctuation)
  - Copy password to clipboard
  - Visual display of generated password and its strength

installation: |
  1. Clone this repository using:
     git clone <your-repo-url>
  2. Navigate into the project directory:
     cd password-generator
  3. Make sure you have Python 3 installed. Tkinter comes included with standard Python distributions.

usage: |
  1. Run the Python script:
     python password_generator.py
  2. Enter the desired password length.
  3. Select a difficulty level: Easy, Medium, or Hard.
  4. Click Generate to create the password.
  5. View the password and its strength.
  6. Click Copy Password to copy it to your clipboard.

future_enhancements:
  - Ensure at least one character of each type in generated passwords
  - Real-time password strength updates while entering options
  - Save generated passwords to a local file securely
  - Web-based version using Flask or Django

license: "This project is open-source and free to use."

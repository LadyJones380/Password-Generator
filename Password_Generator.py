# Password Generator

# Write a password generator in Python.  Be creative with how you generate
# passwords.  Strong passwords have a mix of lowercase letters, uppercase
# letters, numbers and symbols.  The passwords should be random, generating
# a new password every time the user asks for a new password.  Include your
# run-time code in a main method.  Next, ask the user how strong they want
# their password to be.  For weak passwords, pick a word or two from a list.

# Import necessary modules.  The secrets module allows you to generate
# sequences of random numbers that are secure for cryptographic applications.
# You can use functions like choice(), randbits() and randbelow() to generate
# secure random numbers.

import secrets
import string

# Define our alphabet.  This denotes the set of all characters that we'll
# consider for password generation.  Here, we want it to contain the
# following: lowercase, uppercase letters and special characters.

letters = string.ascii_letters # concatenation of lower & uppercase letters.
digits = string.digits # the string concatenation of numbers '0123456789'
special_chars = string.punctuation #string of all special characters

# Finally, let's concatenate the above string constants to get the alphabet:

alphabet = letters + digits + special_chars

# Have user select length of password.  If less than 12, warn user:

pwd_length = int(input("Please select length of password: "))

while pwd_length < 12:
    print("Your password should be a minimum of 12 characters for security.")
    pwd_length = int(input("Please select length of password. "))
else:
    print("Thank you.")

# Generate a password and verify that the password meets certain criteria.
# Check for one special character and at least two digits:

while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd) and
        sum(char in digits for char in pwd)>=2):
            break

print("Here is your password:", pwd)

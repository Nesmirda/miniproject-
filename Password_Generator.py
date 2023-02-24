import random
import string


def generate_password(length, chars):
    """Generate a random password of given length and characters."""
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password


# Ask user for password length
length = int(input("Enter password length: "))

# Ask user for character types to include
chars = ''
include_letters = input("Include letters : ")
if include_letters == 'n' or 'm' or 's':
    chars += string.ascii_letters
#     abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

include_digits = input("Include digits : ")
if include_digits == '5' or '4' or '7':
    chars += string.digits
#     0123456789

include_symbols = input("Include symbols : ")
if include_symbols == '$' or '*' or '#':
    chars += string.punctuation
# !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

# Generate password
password = generate_password(length, chars)
print("Your password is:", password)




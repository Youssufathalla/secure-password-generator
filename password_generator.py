import sys
import secrets
from math import log2

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "!@#$%&*^|()_+"

def get_available_chars(include_upper, include_digit, include_special):
    available = alpha
    if include_upper:
        available += alpha.upper()
    if include_digit:
        available += num
    if include_special:
        available += special
    return available

def main_menu():
    while True:
        try:
            option = int(input('''-- Password Generator --
        Choose option:
        1: Generate password
        2: Exit the program
        Your choice: '''))
        except ValueError:
            print('Invalid input. Please enter 1 or 2.')
            continue

        if option == 1:
            password_type_menu()
        elif option == 2:
            print('Password generator exited.')
            sys.exit()
        else:
            print('Invalid option. Please enter 1 or 2.')

def password_type_menu():
    while True:
        try:
            length = int(input('Please provide password length: '))
            if length <= 0:
                print('Password length must be greater than 0.')
                continue
            break
        except ValueError:
            print('Invalid input. Password length must be a number.')

    while True:
        include_upper_input = input('Use uppercase letters? (y/n): ').lower().strip()
        if include_upper_input == 'y' or include_upper_input == 'n':
            include_upper = include_upper_input == 'y'
            break
        print('Invalid input. Please enter y or n.')

    while True:
        include_digits_input = input('Use digits? (y/n): ').lower().strip()
        if include_digits_input == 'y' or include_digits_input == 'n':
            include_digits = include_digits_input == 'y'
            break
        print('Invalid input. Please enter y or n.')

    while True:
        include_special_input = input('Use special characters? (y/n): ').lower().strip()
        if include_special_input == 'y' or include_special_input == 'n':
            include_special = include_special_input == 'y'
            break
        print('Invalid input. Please enter y or n.')

    selected_categories = 1 + include_upper + include_digits + include_special

    if length < selected_categories:
        print(f'Password length must be at least {selected_categories} to include all selected character types.')
        return

    password = generate_password(length, include_upper, include_digits, include_special)
    strength_score, entropy, strength_label = password_strength_calculator(length, include_upper, include_digits, include_special)

    print('\nGenerated password:', password)
    print('Password strength:', strength_label)
    print('Entropy:', entropy, 'bits')
    print('Strength score:', strength_score, '/ 100')

def generate_password(length, include_upper, include_digits, include_special):
    password_chars = [secrets.choice(alpha)]

    if include_upper:
        password_chars.append(secrets.choice(alpha.upper()))
    if include_digits:
        password_chars.append(secrets.choice(num))
    if include_special:
        password_chars.append(secrets.choice(special))

    available_chars = get_available_chars(include_upper, include_digits, include_special)

    while len(password_chars) < length:
        password_chars.append(secrets.choice(available_chars))

    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

def password_strength_calculator(length, include_upper, include_digits, include_special):
    charset_size = len(alpha)
    if include_upper:
        charset_size += len(alpha)
    if include_digits:
        charset_size += len(num)
    if include_special:
        charset_size += len(special)

    entropy = int(log2(charset_size) * length)
    strength_score = min(entropy, 100)

    if entropy < 40:
        strength_label = 'Weak'
    elif entropy < 70:
        strength_label = 'Moderate'
    elif entropy < 100:
        strength_label = 'Strong'
    else:
        strength_label = 'Very Strong'

    return strength_score, entropy, strength_label

if __name__ == '__main__':
    main_menu()
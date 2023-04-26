import random
import string
import inquirer


def generate_password(max_len: int, include_special_chars: bool = False, include_numbers: bool = False)->str:
    password = ''
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters
    has_digits = False
    has_special = False
    criteria = has_digits and has_special

    if include_special_chars:
        chars += special
    if include_numbers:
        chars += digits

    while not criteria and len(password) < max_len:
        choosen_character = random.choice(chars)
        if choosen_character in digits:
            has_digits = has_special and True
        if choosen_character in special:
            has_special = has_digits and True    
        password += choosen_character

    return password


if __name__ == "__main__":
    questions = [
        inquirer.Text('length', message='How many characters does your password need to have?'),
        inquirer.List('include_special', message='Include special characters?', choices=['yes', 'no']),
        inquirer.List('include_numeric', message='Include numeric characters?', choices=['yes', 'no']),
    ]
    answer = inquirer.prompt(questions)
    max_len = int(answer['length'])
    specials = answer['include_special'] == 'yes'
    numbers = answer['include_numeric'] == 'yes'

    print(f'Your password is: {generate_password(max_len, specials, numbers)}')

import random


def password_generator():
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '-', '+', '=', '[', '{', '}', ']', ';', ':', '/"', '|', '<', ',', '>', '.', '?', '/']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_list = []

    for _ in range(2, 8):
        password_list.append(random.choice(lowercase_letters))
        password_list.append(random.choice(uppercase_letters))
        password_list.append(random.choice(symbols))
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += char

    return password

'''
   Author: Davlatbek Kobiljonov
   Copyright: 23/07/2023 at 1:30 AM
'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")
number_of_letters = int(input("How many letter you want to have in your password? "))
number_of_numbers = int(input("How many numbers you want to have in your password? "))
number_of_symbols = int(input("How many symbols you want to have in your password? "))

# Easy level

easy_password = []
for letter in range(0, number_of_letters):
    easy_password.append(random.choice(letters))
for number in range(0, number_of_numbers):
    easy_password.append(random.choice(numbers))
for symbol in range(0, number_of_symbols):
    easy_password.append(random.choice(symbols))
# Here as you can see all items are just appended to the end of the list
# But that is not so strong password, hackers can easily hack it using some patterns,
# that is why in below I provided hard password generator with a bit of effort
print(f"Your password: {''.join(easy_password)}")

# Now, here I could've used the method called shuffle from random module, but then I decided to create my own algorithm

# random.shuffle(easy_password)
# print(f"Shuffled one: {''.join(easy_password)}")

# Here's what I got.

# hard level

hard_password = []
length_of_password = number_of_letters + number_of_numbers + number_of_symbols
for i in range(0, length_of_password):
    hard_password.append(" ")
# print(f"length of hard password: {len(hard_password)}")

count_chars = 0
while True:
    random_index = random.randint(0, len(hard_password) - 1)
    if hard_password[random_index] == " ":
        hard_password[random_index] = random.choice(letters)
        count_chars += 1
    if count_chars == number_of_letters:
        break
count_chars = 0
while True:
    random_index = random.randint(0, len(hard_password) - 1)
    if hard_password[random_index] == " ":
        hard_password[random_index] = random.choice(numbers)
        count_chars += 1
    if count_chars == number_of_numbers:
        break
count_chars = 0
while True:
    random_index = random.randint(0, len(hard_password) - 1)
    if hard_password[random_index] == " ":
        hard_password[random_index] = random.choice(symbols)
        count_chars += 1
    if count_chars == number_of_symbols:
        break

print(f"Your password: {''.join(hard_password)}")



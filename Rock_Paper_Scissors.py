import random

# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

all_combinations = [rock, paper, scissors]

print("What do you choose?, enter 0 for rock, 1 for paper, 2 for scissors ", end="")
user_choice = int(input())

print("Your choice:")

print(all_combinations[user_choice])

computer_choice = random.randint(0, 2)

print("Computer's choice: ")

print(all_combinations[computer_choice])

# 0 = rock
# 1 = paper
# 2 = scissors

if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You won!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("Computer wins!")








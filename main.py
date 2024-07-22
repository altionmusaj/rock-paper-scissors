rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_choice > 2:
    print("Wrong input. Please enter a number between 0 and 2.")
else: 
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if computer_choice == user_choice:
        print("Draw.")
    elif computer_choice == 0 and user_choice == 1:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print ("You lose.")
    elif computer_choice == 1 and user_choice == 0:
        print("You lose.")
    elif computer_choice == 1 and user_choice == 2:
        print ("You win!")
    elif computer_choice == 2 and user_choice == 0:
        print("You win!")
    else:
        print("You lose.")
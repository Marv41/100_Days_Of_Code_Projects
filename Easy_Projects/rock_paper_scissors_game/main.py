import random


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

list1 = [rock,paper,scissors]
list2 = ["rock","paper","scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").lower())
computer_choice = random.randint(0,2)

if user_choice > 2:
    print("Invalid Choice")
else:
    print(f"User chose: {list2[user_choice]}")
    print(list1[user_choice])
    print(f"Computer chose: {list2[computer_choice]} ")
    print(list1[computer_choice])

    if computer_choice == user_choice:
        print("Tie")
    elif user_choice == 0 and computer_choice == 2:
        print("You WIN!!!")
    elif user_choice == 1 and computer_choice == 0:
        print("You WIN!!!")
    elif user_choice == 2 and computer_choice == 1:
        print("You WIN!!!")
    else:
        print("You Lose")


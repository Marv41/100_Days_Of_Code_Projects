print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

input1 = input("You're at a cross road. Where do you want to go?\n"
               "Type left or right\n")

if input1.lower() == "left":
    input2 = input("Your come to a lake. There is an island in the middle of the lake\n Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if input2.lower() == "wait":
        input3 = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you chose?\n")
        if input3.lower() == "yellow":
            print("You Win!")
        elif input3.lower() == "Red":
            print("Burned by fire. GAME OVER")
        elif input3.lower() == "Blue":
            print("Eaten by beasts. GAME OVER")
        else:
            print("GAME OVER")
    else:
        print("You were attached by a trout. GAME OVER")

else:
    print("You fell into a hole. GAME OVER")







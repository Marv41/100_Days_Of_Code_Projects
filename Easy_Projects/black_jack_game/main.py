import random
import art


continue_playing = True

# Function to check for aces in hand
def check_for_aces(hand_list, count):
    for card in range(len(hand_list)):
        if count > 21 and hand_list[card] == 11:
            hand_list[card] = 1
            count -= 10
    return count

# Function to count current hand
def count_hand(hand_list):
    return sum(hand_list)

# Function to draw a number of cards and add them to a hand
def draw_card(current_hand, requested_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for new_card in range(requested_cards):
        current_hand.append(random.choice(cards))
    return current_hand

choice2 = input("Do you want to play Blackjack? (Yes / No)").lower()
while continue_playing:
    print(art.logo)
    player_bust = False
    dealer_bust = False
    players_hand = []
    computers_hand = []
    players_count = 0
    dealers_count = 0

    draw_card(players_hand,2)
    draw_card(computers_hand, 2)

    if players_count > 21:
        players_count = check_for_aces(players_hand,players_count)

    print(f"Your Hand: {players_hand}, current score: {count_hand(players_hand)}")
    print(f"Computer's first card: {computers_hand[0]} current score: {computers_hand[0]}")

    if players_count == 21:
        print(f"Your Hand: {players_hand}, current score: {players_count}")
        print(f"Computer's first card: {computers_hand[0]} current score: {computers_hand[0]}")
        print("Blackjack You WIN!!!")
        break

    choice = input("Hit or Stay?").lower()
    print("")

    while choice == "hit" and not player_bust:
        draw_card(players_hand,1)
        players_count = count_hand(players_hand)

        if players_count == 21:
            print(f"Your Final Hand: {players_hand}, current score: {players_count}")
            print(f"Computer's Final Hand: {computers_hand} current score: {count_hand(computers_hand)}")
            print("Blackjack You WIN!!!")
            break
        elif players_count > 21:
            players_count = check_for_aces(players_hand, players_count)
            print(f"Your Hand: {players_hand}, current score: {players_count}")
            print(f"Computer's first card: {computers_hand[0]} current score: {computers_hand[0]}")
            print("")

            if players_count > 21:
                player_bust = True
                print(f"Your Final Hand: {players_hand}, current score: {players_count}")
                print(f"Computer's Final Hand: {computers_hand} current score: {count_hand(computers_hand)}")
                print("Bust GAME OVER!!!")
            else:
                choice = input("Hit or Stay?").lower()
                print("")
        else:
            print(f"Your Hand: {players_hand}, current score: {players_count}")
            print(f"Computer's first card: {computers_hand[0]} current score: {computers_hand[0]}")
            choice = input("Hit or Stay?").lower()
            print("")

    if choice == "stay":
        dealers_count = count_hand(computers_hand)
        print(f"Your Hand: {players_hand}, current score: {players_count}")
        print(f"Computer's Hand: {computers_hand} current score: {dealers_count}")
        print("")

        while dealers_count < 17:
            dealers_count = count_hand(draw_card(computers_hand, 1))
            if dealers_count > 21:
                 dealers_count = check_for_aces(computers_hand,dealers_count)
                 print(f"Computer's Hand: {computers_hand} current score: {dealers_count}")
                 print("")
                 if dealers_count > 21:
                    dealer_bust = True

        print(f"Your Final Hand: {players_hand}, current score: {players_count}")
        if dealers_count == 21:
            print(f"Computer's Hand: {computers_hand} current score: {dealers_count}")
            print("Dealer Blackjack You Lose!!!!")

        elif dealer_bust:
            print(f"Computer's Hand: {computers_hand} current score: {dealers_count}")
            print("You Win!!!!")

        elif players_count > dealers_count:
            print(f"Computer's Hand: {computers_hand} current score: {dealers_count}")
            print("You Win!!!!")

        elif players_count < dealers_count:
            print(f"Computer's Hand: {computers_hand} current score: {dealers_count}")
            print("You Lose!!!!")

        else:
            print(f"Computer's Hand: {computers_hand} current score: {dealers_count}")
            print("DRAW!!!!")


    print("")
    choice2 = input("Do you want to play Blackjack? (Yes / No)").lower()
    if choice2 == "no":
        continue_playing = False
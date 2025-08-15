import art

print(art.logo)
bids = {}

more_bidders = True
while more_bidders:
    name = input("What is your name? ")
    bid = input("What is your bit? $")
    bids[name] = bid
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.")


    if yes_or_no == "no":
        more_bidders = False
        winner = max(bids, key = bids.get)
        print(f"The Winner is {winner} with a bid of ${bids[winner]} ")
    else:
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" * 20)

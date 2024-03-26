from art import logo
import os
print(logo)

all_user_bid = {}
bidding_finished = False # Boolean to be able to run thw while loop.

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")

# Taking user inputs
while not bidding_finished:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    all_user_bid[user_name] = user_bid
    # Try to break the loop if there is no other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(all_user_bid)
    elif should_continue == "yes":
        os.system('clear')


print(all_user_bid)

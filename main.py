from clear import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the silent auction!")
total_bids = {}

# add users to hidden bid list
def new_entry(user_name, bid_amount):
    total_bids[user_name] = bid_amount


# determine winner
def top_bid(total_bids):
    values = list(total_bids.values())
    keys = list(total_bids.keys())
    return keys[values.index(max(values))]


proceed = True

while proceed:
    user_name = input("What is your name?: \n")
    bid_amount = int(input("How much would you like to bid?: \n$"))
    other_users = input("Are there any other people looking to bid on this item? Please type 'yes' or 'no' \n".lower())
    if other_users == 'yes':
        new_entry(user_name, bid_amount)
        clear()
    elif other_users == "no":
        new_entry(user_name, bid_amount)
        proceed = False
        clear()
    else:
        print("Invalid entry, please try again.")

top_bidder = top_bid(total_bids)
top_bid_amount = total_bids[top_bidder]

clear()
print(logo)
print(f"{top_bidder} has won the auction with ${top_bid_amount}! \n")
print(f"Total bid list: {total_bids} \n")

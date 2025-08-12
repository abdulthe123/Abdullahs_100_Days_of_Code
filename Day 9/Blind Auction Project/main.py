# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

auctionBids = {}
auctionOver = False

while not auctionOver:
    bidder = input("What is your name? ")
    bid = int(input("How much would you like to bid?: $"))
    auctionBids = {
        bidder: bid
    }
    checkpoint = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    if checkpoint == "no":
        auctionOver = True
    print("\n" * 20)

highestBid = max(auctionBids.values())

for key, value in auctionBids.items():
    if value == highestBid:
        highestBidder = key
        break

print(f"The winner is {highestBidder} with a bid of ${highestBid}")
#Define base prices
price=100
discount=0.1
itemsSold=50

#Calculate prices with discounts
finalPrice=price*(1-discount)
message="Total items sold " + str(itemsSold)

#Check if user is member
isMember=False
memberDiscount=0.1

#Print final calculations
print("Final price " + str(finalPrice))
print(message)
print("Membership discount applied" + str(isMember))
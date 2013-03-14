amount = input("Enter the amount of money: ")
amount *= 100

QUARTER = 25
DIME = 10
NICKEL = 05
PENNY = 01

change = [QUARTER, DIME, NICKEL, PENNY]
coinsUsed = [0, 0, 0, 0]

for currentCoin in range(0, len(change)):
    while(amount - change[currentCoin] >= 0.0):
        coinsUsed[currentCoin] += 1
        amount -= change[currentCoin]


print "Quarters: " + str(coinsUsed[0])
print "Dimes: " + str(coinsUsed[1])
print "Nickels: " + str(coinsUsed[2])
print "Pennies: " + str(coinsUsed[3])
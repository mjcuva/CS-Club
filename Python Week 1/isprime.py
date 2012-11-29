# Output To User
number = input("Enter a number: ")

# Start loop counter
i = 2
prime = True

# Check every number to see if it is divisible
while(i < number and prime == True):
    if(number % i == 0):
        prime = False
        i += 1
    else:
        i += 1

# If we couldn't find a divisible number
if prime == True:
    print str(number) + " is prime"

# If we found a number
else:
    print str(number) + " isn't prime"
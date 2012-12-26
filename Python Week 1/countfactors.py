# Output To User
number = input("Enter a number: ")

# Start loop counter
i = 1
count = 0

# Check every number to see if it is divisible
while(i <= number):
    if(number % i == 0):
        if(i * i == number):
            count += 2
        else:
            count += 1
        print i

    i += 1

print str(number) + " has " + str(count) + " factors." 


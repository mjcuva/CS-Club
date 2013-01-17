inFile = open('input.txt')

lines = inFile.readlines() # Creates array on lines

for line in lines:
    newLine = line.split()[::-1] # The third number is a selector, 2 gives every other, -1 reverses
    newLine = " ".join(newLine) # Join takes the array and places a space between every element
    newLine += "\n" # Adds new line after each line
    print newLine # Write the line to the output file
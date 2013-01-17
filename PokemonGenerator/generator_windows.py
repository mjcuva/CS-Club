import random, webbrowser, os

pokemonList = []
numbers = []

num = raw_input("Enter the number of Pokemon: ")

#Creates the random pokemon numbers
for i in range(0, int(num)):
	numbers.append(random.randint(1, 649))


#Loads list of pokemon
pokemonFile = open("pokemon.txt")

#Puts pokemon into a python list
for pokemon in pokemonFile:
	pokemonList.append(pokemon.strip())

#Prints the pokemon for the generated numbers
for k in numbers:
	print pokemonList[k] + " " + str(k + 1)
	os.startfile('./Pictures/' + str(k + 1) + '.png')
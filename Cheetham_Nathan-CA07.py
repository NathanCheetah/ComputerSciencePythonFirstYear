#Cheetham_Nathan UniversityOfLiverpool 201720385 Cheetham_Nathan-CA07 December2023 Cheetham_Nathan-CA07.py
#This is a program that uses a 2d-array to transform input data into information in the form of a ‘dashboard’ for theatre management

import math #importing of math module for .ceil to round up
import random #importing of random module .randint to generate a random number


#INPUTS
#Cost of production, price of band-A seat, price of band-B seat
def inputs():
	costOfProd = int(input("What is the cost of production: "))
	costOfA = int(input("What is the cost of a band-A seat: "))
	costOfB = int(input("What is the cost of a band-B seat: "))
	return costOfProd, costOfA, costOfB

#PROCESS
# Full House (all seats sold)
def fullHouse():
	row = 4
	col = 5
	Aseats = 10
	Bseats = 10
	seatsMatrix = [[True for x in range(col)] for x in range(row)] #creates a 5 by 4 matrix with all seats set to True (as in taken)
	return Aseats, Bseats, seatsMatrix

# Part House (some seats sold) Randomly chosen
def partHouse():
	row = 4
	col = 5
	row1Number = random.randint(0,5)
	row2Number = random.randint(0,5)
	Aseats = row1Number + row2Number 
	row3Number = random.randint(0,5) 
	row4Number = random.randint(0,5)  
	Bseats = row3Number + row4Number 
	array1 = random1dArray(row1Number)
	array2 = random1dArray(row2Number)
	array3 = random1dArray(row3Number)
	array4 = random1dArray(row4Number)
	seatsMatrix = [array1, array2, array3, array4] #creates a 5 by 4 matrix with all the different 1d arrays
	return Aseats, Bseats, seatsMatrix

# Randomly generates 1d array for Part House
def random1dArray(trues):
    array1d = [False] * 5 #makes the initial 1d array with 5 values storeable

    positions = random.sample(range(5), min(trues, 5)) #places the number of Trues in random places
    for count in positions:
        array1d[count] = True
    return array1d

#OUTPUTS
# Dashboard design of output
def output(prodCost, costA, costB, fullA, fullB, partA, partB, seatsFullMatrix, seatsPartMatrix):
	print("Production cost: £" + str(prodCost))
	print("Cost of class A seat: £" + str(costA))
	print("Cost of class B seat: £" + str(costB))

	fullHouseRev = (costA * fullA)+(costB * fullB) #revenue on full house
	print("\n Full House Revenue:")
	print("Band-A: " + str(fullA) + " seats sold at £" + str(costA) + " per seat = £" + str(costA * fullA))
	print("Band-B: " + str(fullB) + " seats sold at £" + str(costB) + " per seat = £" + str(costB * fullB))
	print("Revenue: £" + str(fullHouseRev))
	fullEven = math.ceil(prodCost / fullHouseRev) #rounding up of days to break even on full house, math.ceil to round up 
	print("Number of shows to break even = " + str(fullEven))


	partHouseRev = (costA * partA)+(costB * partB) #revenue on part house
	print("\n Part House Revenue:")
	print("Band-A: " + str(partA) + " seats sold at £" + str(costA) + " per seat = £" + str(costA * partA))
	print("Band-B: " + str(partB) + " seats sold at £" + str(costB) + " per seat = £" + str(costB * partB))
	print("Revenue: £" + str(partHouseRev))
	partEven = math.ceil(prodCost / partHouseRev) #rounding up of days to break even on part house 
	print("Number of shows to break even = " + str(partEven))

	print("\n Full House seating:") #prints out matrix for full house seating
	for rowFull in seatsFullMatrix:
    print(rowFull)

    print("\n Part House seating:") #prints out matrix for part house seating
	for rowPart in seatsPartMatrix:
    print(rowPart)


def main(): #calls all the functions
	prodCost, costA, costB = inputs()
	fullA, fullB, seatsFullMatrix = fullHouse()
	partA, partB, seatsPartMatrix = partHouse()
	output(prodCost, costA, costB, fullA, fullB, partA, partB, seatsFullMatrix, seatsPartMatrix)


main() #calls main function

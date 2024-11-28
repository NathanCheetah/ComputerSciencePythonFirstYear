#Cheetham_Nathan UniversityOfLiverpool 201720385 Cheetham_Nathan-CA07 December2023 Cheetham_Nathan-CA07.py
#This is a program that uses a 2d-array to transform input data into information in the form of a ‘dashboard’ for theatre management

import math #importing of math module for .ceil to round up
import random #importing of random module .randint to generate a random number

# Use of 2D arrays to turn input into a 'dashboard'

#INPUTS
#Cost of production, price of band-A seat, price of band-B seat
def inputs():
	costOfProd = int(input("What is the cost of production: "))
	costOfA = int(input("What is the cost of a band-A seat: "))
	costOfB = int(input("What is the cost of a band-B seat: "))
	return costOfProd, costOfA, costOfB

#Band A = Band B * 2
# Band A - Row1 (seat 1-5), Row2(seat 6-10)
# Band B - Row3 (seat 11-15), Row4(seat 16-20)


#PROCESS
#break-even = (production cost/revenue) rounded up

# Full House (all seats sold) - How many days to break even
def fullHouse(costOfProd, costOfA, costOfB):
	nSeats = 10
	bandA = nSeats * costOfA
	bandB = nSeats * costOfB
	fullRevenue = bandA + bandB
	fullBreakEven = math.ceil(costOfProd / revenue)
	return bandA, bandB, fullRevenue, fullBreakEven

# Part House (some seats sold) - How many days to break even - Randomly chosen
def partHouse(costOfProd, costOfA, costOfB):
	row1num = random.randint(0,5)
	row1total = row1num * costOfA
	row2num = random.randint(0,5)
	row2total = row2num * costOfA
	row3num = random.randint(0,5)
	row3total = row3num * costOfB
	row4num = random.randint(0,5)
	row4total = row4num * costOfB
	bandAseats = row1num + row2num
	bandBseats = row3num + row4num
	partRevenue = ((bandAseats*costOfA)+(bandBseats*costOfB))
	partBreakEven = math.ceil(costOfProd / revenue)
	return row1total, row2total, row3total, row4total, partRevenue, partBreakEven



#OUTPUT
# Dashboard example
# £ (or your own currency)
# Production cost = x

# Full house revenue:
# Band-A: n-seats sold at £x per seat = x
# Band-B: n-seats sold at £x per seat = x
# Revenue: total for one full house = x
# Number of shows to break-even = x (round this figure up)

# Part-house revenue:
# Band-A: n-seats sold at £x per seat = x
#  Row 1: n-seats sold + total income
#  Row 2: n-seats sold + total income
# Band-B: n-seats sold at £x per seat = x
#  Row 3: n-seats sold + total income
#  Row 4: n-seats sold + total income
# Revenue: total for one part house = x
# Number of shows to break-even = x (round this figure up)
def output():

#EXTRA OUTPUT
# Output all the seats sold as an array
# Output all the partially sold seats as an array

def main(): #calls all the functions


main() #calls main function
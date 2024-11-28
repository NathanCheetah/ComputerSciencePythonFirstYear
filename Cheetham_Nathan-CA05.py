#Cheetham_Nathan UniversityOfLiverpool 201720385 Cheetham_Nathan-CA05 November2023 Cheetham_Nathan-CA05.py
#This a program to check if a number is odd and/or prime, and to calculate the volume of an ice floe


def prime_odds(primeOddInput): #checks if prime and/or odd
	odd = False
	prime = True

	if((primeOddInput % 2) != 0): #checks if odd
		odd = True

	if(primeOddInput > 1): #checks for numbers it can be divisible by without remainder, that isn't itself
		for counter in range(2, primeOddInput-1):
			if((primeOddInput % counter) == 0):
				prime = False

	if(prime and odd): #chooses output to give
		print("The integer you have inputted is a prime number and an odd number")
	elif(prime and not odd):
		print("The integer you have inputted is a prime number and not an odd number")
	elif(not prime and odd):
		print("The integer you have inputted is not a prime number and is an odd number")
	else:
		print("The integer you have inputted is not a prime number nor odd number")

	return " "


def floe_input(): #takes inputs and send to process
	freeboard = int(input("Enter the freeboard height: "))
	length = int(input("Enter the length of the ice: "))
	width = int(input("Enter the width of the ice: "))
	return freeboard, length, width

def floe_process(freeboard,length,width): #calculations on floe to get volume to output
	thickness = freeboard * 9
	volume = thickness * length * width
	return volume

def floe_output(volume): #output from function
	print(volume)


def main(): #calls all the functions
	checkPrimeOdd = int(input("Input an int: "))
	prime_odds(checkPrimeOdd) #calls function with arg

	print("Now running the floe program...")
	freeboard, length, width = floe_input() #puts values from input into process args
	volume = floe_process(freeboard, length, width) #puts return value from process into output arg
	floe_output(volume)


main() #calls main function
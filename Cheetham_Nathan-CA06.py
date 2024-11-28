#Cheetham_Nathan UniversityOfLiverpool 201720385 Cheetham_Nathan-CA06 November2023 Cheetham_Nathan-CA06.py
#This a program to create an alien name from family and given name

#Alien Name Algorithm
# Take actor name in form: first, last
# Take first 2 letters of first name
# Take first 3 letters of last name
# Add 3 letters from last with 2 letters from first after it 

#OUTPUT FORMAT:
# actor name	character name


def given(): #brings in given name list
	actorGivenList = ['andrei','harry','yuan','sadiq','zeng']
	return actorGivenList

def family(): #brings in family name list
	actorFamilyList = ['stephens','venables','spield','elbahi','ergan']
	return actorFamilyList

def given_2chars(givenList): #splits given name into first 2 letters
	given2chars = []

	for name in givenList:
		twoChars = name[:2]
		given2chars.append(twoChars)
	return given2chars


def family_3chars(familyList): #splits family name into first 3 letters
	family3chars = []

	for name in familyList:
		threeChars = name[:3]
		family3chars.append(threeChars)
	return family3chars


def alien_list(family3, given2): #creating of alien name
	alienList = []

	for name in range(len(family3)):
		alienName = family3[name] + given2[name]
		alienList.append(alienName)

	return alienList


def director_name(alienList): #creates name "steven spielburg" as director, had some issues with putting space between his name hence the long method
	directorHold = ""
	for name in alienList:
			directorHold = directorHold + name[:3]

	directorGiven = directorHold[:6]
	directorFamily = directorHold[6:]

	director = directorGiven + " " + directorFamily

	return director


def output_lists(givenList, familyList, alienList, director): #outputting of new list
	print("Director:")
	print(director)
	print("\n")

	print("Actors: \t \t Alien Name:")
	for name in range(len(givenList)):
		actorName = givenList[name] + " " + familyList[name]
		print(actorName + "\t \t" + alienList[name])


def main(): #calls all the functions
	givenList=[]
	familyList=[]
	given2Chars=[]
	family3Chars=[]
	alienList=[]

	givenList = given()
	familyList = family()

	given2Chars = given_2chars(givenList)
	family3Chars = family_3chars(familyList)

	alienList = alien_list(family3Chars, given2Chars)
	director = director_name(alienList)

	output_lists(givenList, familyList, alienList, director)


main() #calls main function

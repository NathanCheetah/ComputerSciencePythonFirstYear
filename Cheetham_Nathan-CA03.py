#Cheetham_Nathan UniversityOfLiverpool 201720385 Cheetham_Nathan-CA03 October2023 Cheetham_Nathan-CA-03.py
#A program to convert cat years and month to human years


#Menu output
print("""
	Cat Age Main Menu
	A. Months 8 to 24
	B. Years 3 to 6
	X. Exit Program
	""")
menuInput = input("Enter Option(A/B/X): ")


#Checking menu inputs
if(menuInput == "A"): #If menu A option - Junior Years
	monthInput = int(input("Enter your cat's age in months: "))
	if(monthInput < 25 and monthInput > 7):
		#calc of human years from cat months
		humanAge = monthInput + 3
		print(f"Your cat is in their Junior Life-Stage, they are {humanAge} human years")
	else:
		print(f"Error - The input {monthInput} is outside the range of 8 to 24 months")

elif(menuInput == "B"): #If menu B option - Prime years
	yearInput = int(input("Enter your cat's age in years: "))
	if(yearInput < 7 and yearInput > 2):
		#calc of human years from cat years
		humanAge = ((yearInput - 3) * 4) + 28
		print(f"Your cat is in their Prime Life-Stage, they are {humanAge} human years")
	else:
		print(f"Error - The input {yearInput} is outside the range of 3 to 6 years")

elif(menuInput == "X"): #If menu option X for end is chosen
	print("Ending program...")

else: #If menu input is an error
	print("Input error - Program ending")


#Testing key: SAE(Same as expected)

#Test   / inputs(a,b) 	/ expected(c,d)                  					   	       / actual              / comment
#-------/-------------	/--------------------------------------------------------------/---------------------/---------------
#MENU OPTION A TESTING
#1      / A, 8		  	/ "Enter your cat's age in months:", "Junior Life-Stage... 11" / SAE, SAE            / Ok
#2      / A, 12   	  	/ "Enter your cat's age in months:", "Junior Life-Stage... 15" / SAE, SAE 			 / Ok
#3      / A, 24       	/ "Enter your cat's age in months:", "Junior Life-Stage... 27" / SAE, SAE 			 / Ok
#4      / A, 13       	/ "Enter your cat's age in months:", "Junior Life-Stage... 16" / SAE, SAE 			 / Ok
#5      / A, 25       	/ "Enter your cat's age in months:", "Error - The input 25..." / SAE, SAE 			 / Ok
#6      / A, 7        	/ "Enter your cat's age in months:", "Error - The input 7..."  / SAE, SAE 			 / Ok

#MENU OPTION B TESTING
#7      / B, 3        	/ "Enter your cat's age in years:", "Prime Life-Stage... 28"   / SAE, SAE 			 / Ok
#8      / B, 5        	/ "Enter your cat's age in years:", "Prime Life-Stage... 36"   / SAE, SAE 			 / Ok
#9      / B, 6        	/ "Enter your cat's age in years:", "Prime Life-Stage... 40"   / SAE, SAE 			 / Ok
#10     / B, 7        	/ "Enter your cat's age in years:", "Error - The input 7..."   / SAE, SAE 			 / Ok
#11     / B, 2        	/ "Enter your cat's age in years:", "Error - The input 2..."   / SAE, SAE 			 / Ok

#MENU OPTION X TESTING
#12     / X 			/ "Ending program..."										   / SAE 				 / Ok

#MENU OPTION INVALID
#13 	/ H 			/ "Input error - Program ending"							   / SAE 				 / Ok
#14 	/ C 			/ "Input error - Program ending"							   / SAE 				 / Ok
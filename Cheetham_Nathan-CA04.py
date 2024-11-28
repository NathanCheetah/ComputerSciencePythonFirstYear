#Cheetham_Nathan November2023 Cheetham_Nathan-CA-04.py
#This a program to calculate the raw grade and final grade from two grades

#Student submits assignments
#Students on register submit assignments in 2 parts, coding and test - 50% each part

#Grading of assignment
#Inputs: Coding(50-100), Test(50-100), DaysLate(0-2)
#Lateness: 1 day-Subtract 5 marks, 2 days-subtract 10 marks
#If submit only 1 then one grade is 0 and other is 50-100(inclusive)

#INPUTS
#How many students to be inputted - no validation
#StudentID - no validation
#Coding grade - validate (50-100 only)
#testing grade - validate (50-100 only)
#days late - validate (0-2 only, treat as typo if wrong and get to reinput) 

#OUTPUTS
#Stud-id
#Coding mark
#Testing mark
#Days late
#Raw grade: (coding grade + test grade)/2
#Final grade : rawGrade - latePenatly

#Loop for number of students
studentInput = int(input("How many students to process: "))
for StudentCount in range(studentInput):
	studentId = StudentCount+1

	#Coding mark input and validation, repeat if wrong
	correctCoding = False
	while(correctCoding == False):
		codingGrade = int(input("Enter coding grade: "))
		if(codingGrade > 49 and codingGrade < 101 or codingGrade == 0):
			correctCoding = True

	#Testing mark input and validation, repeat if wrong
	correctTest = False
	while(correctTest == False):
		testGrade = int(input("Enter testing grade:"))
		if(testGrade > 49 and testGrade < 101 or testGrade == 0):
			correctTest = True

	#Late days input and validation with latePenalty calculation, repeat if wrong
	correctLate = False
	while(correctLate == False):
		lateDays = int(input("Enter amount of days late: "))
		if(lateDays == 0):
			latePenalty = 0
			correctLate = True
		elif(lateDays == 1):
			latePenalty = 5
			correctLate = True
		elif(lateDays == 2):
			latePenalty = 10
			correctLate = True


#Processing of raw and final grade
	rawGrade = (codingGrade + testGrade) / 2
	finalGrade = rawGrade - latePenalty

#Output
	print("StudentId    Coding grade    Test grade    Days late    Raw grade    Final grade")
	print(f"{studentId}    {codingGrade}    {testGrade}    {lateDays}    {rawGrade}    {finalGrade}")
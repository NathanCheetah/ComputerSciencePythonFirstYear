#Cheetham_Nathan UniversityOfLiverpool 201720385 Cheetham_Nathan-CA02 October2023 Cheetham_Nathan-CA-02.py
#A program to calculate the distance moved by a robot rover, including the horizontal and vertical distance from the starting point, as well as the amount of battery used and remaining

import math

#Facts:
#Battery uses 2.7% per second
#Speed = 1.5m/s
#Travel paramters = North to East (0-90 degrees)
#Python deals with angles in radians


#Inputs:

#Angle in degrees (python calculates in radians, use builtin functions)
angle = int(input("Input angle: "))

#Time of travel in seconds
time = int(input("How long does the rover travel: "))


#Process:

#Distance = speed * time
distance = time * 1.5

#Horizontal distance = distance * sine of angle
horizDistance = distance * math.sin(math.radians(angle))

#Vertical distance = distance * cosine of angle
vertDistance = distance * math.cos(math.radians(angle))

#Estimated battery usage = time * battery usage
batteryUse = time * 2.7
if(batteryUse > 100):
	batteryUse = 100

remainingBattery = 100 - batteryUse
if(remainingBattery <= 0):
	remainingBattery = 0


#Outputs:

#Echo back inputs
print(f"Angle: {angle:.3f}degrees  Time: {time:.3f}s")

#Distance travelled
print(f"Total distance travelled is: {distance:.3f}m")

#Horizontal travelled
print(f"The horizontal distance from the start position is: {horizDistance:.3f}m")

#Vertical travelled
print(f"The vertical distance from the start position is: {vertDistance:.3f}m")

#Battery usage
print(f"The percentage of battery used is: {batteryUse:.3f}%")

#Battery remaining
print(f"The percentage of battery remaining is: {remainingBattery:.3f}%")

#Message to user about battery status with respect to the return trip
#Check robot can reach:
#	If not, inform user with relevant data, exit program
#	If yes, inform if it can get back along same path it came from
if(batteryUse >= 100):
	print("There is no battery charge remaining")
elif((batteryUse*2)>100):
	print("There is enough battery to take the path provided, but there is not enough battery to return along the same path")
else:
	print("There is enough battery to take the path provided, and there is enough battery after to return along the same path")


#Test   / inputs(a,b) / expected(c,d,e,f,g,h,i,j)                  / actual                               	     / comment
#-------/-------------/--------------------------------------------/---------------------------------------------/---------------
#1      /1,2    	  /1,2,3,0.052,3,5.4,94.6,"Is enough..."       /1,2,3,0.052,3,5.4,94.6, "Is enough..."	     / Ok
#2      /2,1          /2,1,1.5,0.052,1.499,2.7,97.3,"Is enough.."  /2,1,1.5,0.052,1.499,2.7,97.3,"Is enough.."   / Ok
#3      /0,5          /0,5,7.5,0,7.5,13.5,86.5,"Is enough..."      /0,5,7.5,0,7.5,13.5,86.5,"Is enough..."	     / Ok
#4      /90,5 		  /90,5,7.5,7.5,0,13.5,86.5,"Is enough..."     /90,5,7.5,7.5,0,13.5,86.5,"Is enough..."      / Ok
#5 		/45,45 		  /45,45,67.5,47.73,47.73,100,0,"No battery..."/45,45,67.5,47.73,47.73,100,0,"No battery..." / Ok
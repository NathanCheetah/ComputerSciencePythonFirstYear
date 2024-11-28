#Cheetham_Nathan CA-01.py October2023
#Input three values - Calculate draft of vessel - Output draft, mass, surface area and echo inputs


#Inputs
length = float(input("Enter length of iron barge in metres: "))
breadth = float(input("Enter breadth of iron barge in metres: ")) 
height = float(input("Enter height of iron barge in metres: ")) 
ironWeight = 1.06 #iron weighs 1.06kg per metre squared


#Processing of calculations
surfaceArea = ((length*height)+(breadth*height))*2 + (length*breadth)
mass = ironWeight * surfaceArea
draft = mass / (length * breadth)


#Outputs - rounded to 3 decimal places
print(f"Length: {length} Breadth: {breadth} Height: {height}")#echoing inputs
print(f"Surface Area: {surfaceArea:.3f} metres squared") #output of surface area calculated
print(f"Mass: {mass:.3f} kilograms") #output of mass calculated
print(f"Draft: {draft:.3f} metres") #output of draft calculated


#Limited all the values to 3dp as it gives enough percision

#Test   / inputs(a,b,c)   / expected(d,e,f,g,h,i)                / actual                               / comment
#-------/-----------------/--------------------------------------/--------------------------------------/---------------
#1      / 1,2,3           / 1,2,3,20,21.2,10.6                   / 1,2,3,20,21.2,10.6                   / ok
#2      / 3,1,2           / 3,1,2,19,20.14,6.713                 / 3,1,2,19,20.14,6.713                 / ok
#3      / 7,5,6           / 7,5,6,179,189.74,5.421               / 7,5,6,179,189.74,5.421               / ok
#4      / 33,24,46        / 33,24,46,6036,6398.16,8.078          / 33,24,46,6036,6398.16,8.078          / ok
#5      / 1.2,2.3,3.4     / 1.2,2.3,3.4,26.56,28.154,10.201      / 1.2,2.3,3.4,26.56,28.154,10.201      / ok
#6      / 33.5,24.5,46.5  / 33.5,24.5,46.5,6214.75,6587.635,8.026/ 33.5,24.5,46.5,6214.75,6587.635,8.026/ ok
#7      / j,k,l           / error                                / error                                / ok, should not take in letters 

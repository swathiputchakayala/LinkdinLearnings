# Variable

wallet = 41 ## here wallet is the variable and 41 is value
print(wallet) 

# Numbers : Ints & floats

a = 30
t = -15
c = 30.56
print (t*a)

# String

color = "blue"
shop = "Piza Shop"
print(shop)
print(color,shop)

# Using Variables in strings

day = 25
month ="December"
temp = -10
print ("Today is October 21 and its -15 degrees outside") ## instead of writing the whole text u can use as below
print(f"Today is {month} {day} and its {temp} degress outside")  ## this give the dynamic with respect to the change in varible values

#Booleans and if statements

light_is_on = True
if light_is_on:
    print("The light is on!")
print("Error..tab is missing!")

#comparision and else

Weight = 100
if Weight <= 55:
    print("u r healthy!")
else:
    print("U need to workout!")

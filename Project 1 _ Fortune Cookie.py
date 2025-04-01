# Picking random number
import random
a = random.randint(1,10) 
'''
syntax is ramdom.randint(mix,max).
=> here randint is for printing integer only
1 = min value that to be given in braces & 10 is max value that to be given
'''
print(a)
print(random.random()) # it give float values in the range of 0 to 1

marks = random.randint(0,100)
if marks >= 80:
    print("First Class")
if marks >= 40 and marks <80:
    print("Second Class")
if marks < 40:
    print ("FAIL")
    
    
############################                PROJECT                ############################                PROJECT                ############################


lucky_number = random.randint(1,1000)
fortune_number = random.randint(1,3)
fortune_text = ''
if fortune_number == 1:
    fortune_text = " You will have a great day!!"
if fortune_number == 2:
    print("Atleast not ur worst day!!")
if fortune_number == 3:
    print ("Atleast u r not dead so be greatful")  
print(f"{fortune_text},Your Lucky Number is: {lucky_number}")

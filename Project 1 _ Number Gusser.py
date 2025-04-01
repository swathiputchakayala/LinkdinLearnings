### Game LOOP
import random
import time
print(" Hi! Welcome to the game. You need to guess the number beteween 1 to 100")
time.sleep(3) # it helps in printing the next line delayed by 3 seconds.
print("Are you thinking of the number...!?")
time.sleep(2)
print("Ok! Now its time for you to put guess the number")
time.sleep(1)
guess = int(input("Guess the number!:"))
correct_number = random.randint(1,100)
guess_count = 1
while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong!Guess the higher number!:"))
    else:
        guess = int(input("Wrong!Guess the lower number!:"))
print(f"Yey!! the correct guess is {correct_number} You got right answer in {guess_count} times ! :)")
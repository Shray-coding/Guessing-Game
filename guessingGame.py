import random

number=random.randint(1,9)
chances = 5

while chances!=0:
    guess=int(input("Guess a number between 1 and 9:"))
    if(guess<number):
        print("Guess is too low")
        chances=chances-1
    elif(guess>number):
        print("Guess is too high")
        chances=chances-1
    else:
        print("You guessed it!")
        break
    
if(chances==0):
    print("You lost")



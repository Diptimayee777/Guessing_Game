import random

r=random.randint(1,100)
guess=0

while guess!=r:
    guess=int(input("Enter guess:"))
    if (guess<r):
        print("Guess higher!")
    elif(guess>r):
        print("guess lower!")
    else:
        print("You won!")

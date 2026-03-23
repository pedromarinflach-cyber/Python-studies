import random

secret = random.randint(1, 20)
tries = 0

print("I'm thinking of a number between 1 and 20")

while True:
    text = input("Take a guess: ")
    guess = int(text)
    tries += 1

    if guess < 1 or guess > 20:
        print("That number is out of range. Try again.")
    elif guess < secret:
        print("Too low, try again.")
    elif guess > secret:
        print("Too high, try again.")
    else:
        print("You got it in", tries, "tries!")
        break  

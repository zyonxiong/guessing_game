"""A number-guessing game."""

from random import randint
player_name = input("Howdy, what's your name? ")

print(f"{player_name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

num = randint(1,100)

print(num) #cheatsheet
count = 0

while True:
    # try and except helps handling with error
    try:
        guess = int(input("Your guess? "))
        if guess > 0:
            if guess < num:
                print("Your guess is too low, try again.")
            elif guess > num:
                print("Your guess is too high, try again.")
            else:
                print("Congrats, you got it right!")
                break

    except ValueError:
        print("That's not a valid response. Please try again.")

    count += 1
print(f"Well done {player_name}, it took you {count} times to get it right!")





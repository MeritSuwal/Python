from curses.ascii import isdigit
import random 


max_range = input("Type a number: ")

if max_range.isdigit():
    max_range = int(max_range)

    if max_range <= 0:
        print("Please type a number larger than zero.")
        quit()
else:
    print("Enter a proper number next time.")
    quit()

random_number = random.randint(0, max_range)
guesses = 0

while True:
    guesses +=1
    guess_user = input("Make a guess: ")

    if guess_user.isdigit():
        guess_user = int(guess_user)
    else:
        print("Please guess with a number.")
        continue

    if guess_user == random_number:
        print("You got it correct.")
        break
    elif guess_user > random_number:
        print("You were above the number! ")
    else:
        print("You were below the number")

print(f"YOU GOT IT IN {guesses} GUESSES.")


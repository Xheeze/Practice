#!/usr/bin/python3
import random
secret_number = [1,2,3,4,5,6,7]
random.shuffle(secret_number)
secret_number = random.choice(secret_number)
guess_count = 0
guess_limit = 3
print("WELCOME TO THE GUESSING GAME!!!!!!")
while guess_count < guess_limit:
    guess = int(input("\nGuess a number from 1-7: "))
    guess_count += 1   
    if guess == secret_number:
        print("\n:::::::::::::::::: WOW (0_0):you've won. ::::::::::::::::")
        
        break
else:
    print("\nTry again in the Next game Coz this one is unfortunately LOST.\n")

# input("\nStart a new Game????")    
# if input == "Yes":
#     guess
# else:
#     exit
import random

roll = random.randint(1,10)
guess = 0
guesses = 0

print(f'Randon Number: {roll}')
print("Guess a number between 1 and 10")

while guess != roll:

    guesses += 1

    #print("Enter guess #" + str(guesses) + ": ")
    guess = input("Enter guess #" + str(guesses) + ": ")
    
    if guess.isnumeric() == False:
        print("Numbers only, please!")
    elif int(guess) == roll:
        print(f'You guessed it write in {guesses} tries!')
        break
    elif int(guess) < roll:
        print("Tour guess is too low, try again!")
    else:
        print("Tour guess is too high, try again!")
        
        
    

# This is a guess the number game

import random

print('Hello, What is your name ?')
name = input()

print('Well, ' + name +', I am thinking of a number between 0 and 20')


secretNumber = random.randint(1,20)

# there will be six guesses only, range function start from 1 but it doesn't include 7 
for guessesTaken in range(1,7): 
    print('Take a guess')
    
    # user inputs will be stored in guess variable, we should convert it into number so we can compare it with the secret number 
    
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break # this condition is for the correct guess

if guess == secretNumber:
    print('Good job, ' +name+ '! You guessed my number in ' + str(guessesTaken) + ' guesses !')
else:
    print('Nope, the number i was thinking of was ' + str(secretNumber))



print('You took ' +str(guessesTaken) + ' guesses')

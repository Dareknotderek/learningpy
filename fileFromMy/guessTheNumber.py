#This is a guess the number game taken from Automate the Boring Stuff with a bit more complexity (not much at all) added.
import random
secretNumber=random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess, you have ' + str(7 - guessesTaken) + ' left.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #this condition is the correct guess

if guess==secretNumber:
    print('Good job! You guess the number in ' +str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
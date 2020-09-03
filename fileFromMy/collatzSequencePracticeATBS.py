#Big thanks to stackoverflow on this one for helping me understand recursion, link:
#Write a function named collatz() that has one parameter named number.
#If number is even, then collatz() should print number // 2 and return this value.
#If number is odd, then collatz() should print and return 3 * number + 1.
#Has input validation.

def collatz(number): #main colltaz function
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        number = 3 * number + 1
        print(number)
        return number
try:
    n = input('Enter number: ') # takes user input
    while n !=1: # performs while loop until 'n' becomes 1
        n = collatz(int(n)) # passes 'n' to collatz() function until it arrives at '1'
except ValueError:
    print('Value Error. Please enter integer.')
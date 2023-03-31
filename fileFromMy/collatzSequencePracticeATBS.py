#Big thanks to stackoverflow on this one for helping me understand recursion, and to GPT4 for helping optimize the code
#Performs a Collatz sequence operation on the input number.
#Args: number (int): The number to perform the Collatz operation on.
#Returns: int: The result of the Collatz operation.

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print(result)
    return result

def main():
    try:
        n = int(input('Enter a positive integer: '))
        if n <= 0:
            raise ValueError('The input must be a positive integer.')

        while n != 1:
            n = collatz(n)
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()

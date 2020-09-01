#Has a divide by zero with a try clause to not crash the entire thing
def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument. You tired to divide by zero - this is impossible.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
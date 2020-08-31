#Demonstrates how global statements work within functions using `global [variable]`
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global' #set global, but `spam` overwrites global variable, reassigning 'spam' instead of 'global' for `eggs`
spam()
print(eggs)
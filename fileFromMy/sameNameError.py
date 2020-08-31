#demonstrates error when using a local variable before assigning a value to it
#doesn't fall back on global since it's using a local variable within `spam`
def spam():
    print(eggs) #throws an error
    eggs = 'spam local'

eggs = 'global'
print(eggs)
spam()
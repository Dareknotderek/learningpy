#Demonstrates how global and local variables/parameters work, when they share the same name, and why it's best to avoid
def spam():
    eggs='spam local'
    print(eggs) #prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) #prints 'bacon local'
    spam() #prints 'spam local'
    print(eggs) #prints 'bacon local since it's still in `bacon`

eggs = 'global'
bacon() #prints 'bacon local'x2
print(eggs) #prints 'global'
#Demonstrates wht happens when there are the same local and global names for variables
def spam():
    global eggs #allows for manipulation/assigning global eggs
    eggs = 'spam' #this is global

def bacon():
    eggs = 'bacon' #this is local, and only part of this function

def ham():
    print(eggs) #this is the global

eggs = 42 #this is the global, can be reassigned and is when `spam()` is called
print(eggs) #pre-write with spam()
ham()#pre-write with spam()
spam() #reassigns/overwrites the value of `eggs` to 'spam'
print(eggs) #post-write via spam()
ham()#post-write via spam()
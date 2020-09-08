#Demonstrates how to use a list value to have a single variable instead of the ineloquent version of `allMyCats1.py`

catNames=[]
while True:
    print('Enter the name of cat ' + str(len(catNames) +1) + ' (Or enter nothing to stop.):')
    name = input()
    if name =='':
        break
    catNames = catNames + [name] #list concatenation (adds `name` to the list)
print ('the cat names are:')
for name in catNames:
    print(' ' + name)
#makes a program that moves a few astericks back and forth until `cntrl-c` is keyed
import time, sys
indent=0 #how many spaces to indent
indentIncreasing=True #whether the indentation or increasing or not

try:
    while True: #the mail program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #pause for 1/10 of a second.

    if indentIncreasing:
        #increase the number of space:
        indent = indent+1
        if indent == 20:
            #change direction
            indentIncreasing=False
    else:
        #decrease the number of spaces:
        indent = indent - 1
        if indent==0:
            #change direction
            indentIncreasing=True
except KeyboardInterupt:
    sys.exit()
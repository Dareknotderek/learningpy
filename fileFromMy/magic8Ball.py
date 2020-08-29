#Outlines how Return Values and Return Statements work, with a 'magic 8 ball' as an example
#Imports necessary modules, defines and calls a function with a passed argument/variable, assigns parameters, prints
#Returns the outcome in the function, then requires print to show returned value
import random

def getAnswer(answerNumber):
    if answerNumber==1:
        return 'It is certain'
    elif answerNumber==2:
        return 'It is decidedly so'
    elif answerNumber==3:
        return 'Yes'
    elif answerNumber==4:
        return 'Reply hazy, try again'
    elif answerNumber==5:
        return 'Ask again later'
    elif answerNumber==6:
        return 'Concentrate and ask again'
    elif answerNumber==7:
        return 'My reply is no'
    elif answerNumber==8:
        return 'Outlook no so good'
    elif answerNumber==9:
        return 'Very doubtful'

print(getAnswer(random.randint(1,9)))
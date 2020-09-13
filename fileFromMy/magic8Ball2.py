#Makes a more elegant version of `magic8Ball.py` by using lists
#removes need to use multiple identical `elif` statements

import random #imports random so we can have "random" outputs from asking the 8 ball

messages = ['It is certain', #list that has the messages from the 8 ball
    'it is decidely so',
    'Yes, definitely',
    'Reply hazy, try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages)-1)]) #looks at list of messages, randint picks
#an index number between 0 and the length of messages minus one (so we don't get an error)
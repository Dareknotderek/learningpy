import random

# A list containing the responses from the magic 8 ball
responses = [
    'It is certain',
    'It is decidedly so',
    'Yes, definitely',
    'Reply hazy, try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

def magic_8_ball():
    response = random.choice(responses)  # Selects a random response from the list
    print(response)

if __name__ == "__main__":
    magic_8_ball()

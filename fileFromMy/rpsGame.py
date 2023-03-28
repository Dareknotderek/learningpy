import random, sys

def display_move(move):
    moves_dict = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
    return moves_dict.get(move)

print('ROCK, PAPER, SCISSORS')

# These variables tally outcomes
wins = 0
losses = 0
ties = 0

while True:  # The main game loop
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    # The player input loop
    player_move = ''
    while player_move not in ['r', 'p', 's', 'q']:
        player_move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ").lower()
        if player_move == 'q':
            sys.exit()  # quit the program

    # Display what the player chose:
    print(f'{display_move(player_move)} versus...')

    # Display what the computer chose
    computer_move = random.choice(['r', 'p', 's'])
    print(display_move(computer_move))

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move, computer_move) in [('r', 's'), ('p', 'r'), ('s', 'p')]:
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1

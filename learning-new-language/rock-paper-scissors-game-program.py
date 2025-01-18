import random

options = ('rock', 'paper', 'scissors')
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Choose rock, paper, or scissors: ').lower()

    print(f'You chose {player}.')
    print(f'Computer chose {computer}.')

    if player == computer:
        print('It\'s a tie!')
    elif player == 'rock' and computer == 'scissors':
        print('You win!')
    elif player == 'paper' and computer == 'rock':
        print('You win!')
    elif player == 'scissors' and computer == 'paper':
        print('You win!')
    else:
        print('Computer wins!')

    if input('Do you want to play again? (y/n): ').lower() != 'y':
        running = False

print('Thanks for playing!')
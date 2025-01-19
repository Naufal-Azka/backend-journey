import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print('---------------------------------')
    print(' | '.join(row))
    print('---------------------------------')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print('---------------------------------')
    print("Welcome to the Slot Machine!")
    print('Symbols:  🍒 🍉 🍋 🔔 ⭐  ')
    print('---------------------------------')

    while balance > 0:
        print(f'Current balance: ${balance:.2f}')

        bet = input('Enter your bet: ')
        if not bet.isdigit():
            print('Please enter a valid number')
            continue

        bet = int(bet)
        if bet > balance:
            print('You do not have enough balance')
            continue

        if bet <= 0:
            print('Please enter a valid number')
            continue

        balance -= bet

        row = spin_row()
        print('Spinning...\n')
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            balance += payout
            print(f'Congratulations! You won ${payout:.2f}')
        else:
            print('Sorry, you lost. Try again!')

        play_again = input('Would you like to play again? (y/n): ')
        if play_again.lower() != 'y':
            break
        
    print(f'Game over! Your final balance is ${balance:.2f}')

if __name__ == "__main__":
    main()
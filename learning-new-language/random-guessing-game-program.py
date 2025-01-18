import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Pyton Random Guessing Game")
print(f"Guess a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range.")
            print(f"Please enter a number between {lowest_num} and {highest_num}")
        elif guess > answer:
            print("Try guessing lower.")
        elif guess < answer:
            print("Try guessing higher.")
        else:
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            is_running = False
    else:
        print("Invalid input.")
        print(f"Please enter a number between {lowest_num} and {highest_num}")
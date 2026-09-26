from config import PASSWORD, MAX_ATTEMPTS
from validation import is_valid_guess
from hints import get_hint


def play_game():
    attempt = 1
    success = False

    while attempt <= MAX_ATTEMPTS:

        try:
            guess = int(input("Enter the password: "))

        except ValueError:
            print("Enter a valid number")
            continue

        if guess == PASSWORD:
            print("Bingo!! You guessed it right")
            success = True
            break

        if not is_valid_guess(guess):
            print("Enter a 4 digit number")
        else:
            print(get_hint(guess))

        print(f"Attempts left: {MAX_ATTEMPTS - attempt}")

        attempt = attempt + 1

    if success == False:
        print("Game over! You have used all your attempts")
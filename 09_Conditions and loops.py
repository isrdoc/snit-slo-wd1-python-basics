from random import randint

minimum = 1
maximum = 30

secret = randint(minimum, maximum)
guess = None

did_guess_secret = False

while not did_guess_secret: # While True
    # Do all this
    guess = int(input(f"Guess the secret number (between {minimum} and {maximum}): "))
    did_guess_secret = guess == secret

    if did_guess_secret:
        print(f"You guessed it - congratulations! It's number {secret}.")
        break

    if guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")


print("End")

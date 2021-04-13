from random import randint

minimum = 1
maximum = 30

secret = randint(minimum, maximum)
guess = None
did_guess_secret = False
attempts = 0

while not did_guess_secret:
    attempts += 1
    print(f"This is attempt number {attempts}")
    guess = int(input(f"Guess the secret number (between {minimum} and {maximum}): "))
    did_guess_secret = guess == secret

    if did_guess_secret:
        print(f"You guessed it - congratulations! It's number {secret}.")

        with open("secret_score.txt", "r") as secret_score_file:
            score_in_file = int(secret_score_file.read())
        is_score_better = attempts < score_in_file

        if is_score_better:
            print("Your score is the best score!")
            with open("secret_score.txt", "w+") as secret_score_file:
                secret_score_file.write(str(attempts))

        if not is_score_better:
            print(f"Your score is not the best score. Best score is {score_in_file}")

        break

    if guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")


print("End")

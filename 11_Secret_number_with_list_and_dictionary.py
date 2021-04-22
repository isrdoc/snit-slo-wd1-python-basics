import datetime
from random import randint
import os.path
import json
from helpers import sum_two_numbers


print(sum_two_numbers(1, 2))

minimum = 1
maximum = 30

secret = randint(minimum, maximum)
guess = None
did_guess_secret = False
attempts = 0
score_file = "best_scores.txt"
best_scores = []


class Score:
    def __init__(self, attempts, timestamp):
        self.attempts = attempts
        self.timestamp = timestamp


def write_scores_to_file():
    with open(score_file, "w+") as secret_score_file:
        timestamp = datetime.datetime.now()
        next_score = Score(attempts=attempts, timestamp=timestamp)
        best_scores.append(next_score.__dict__)
        secret_score_file.write(json.dumps(best_scores))


if os.path.isfile(score_file):
    with open(score_file, "r") as secret_score_file:
        best_scores = json.loads(secret_score_file.read())

copy_best_scores = best_scores.copy()
copy_best_scores.sort()

print(f"These are the best scores: {copy_best_scores[:3]}")

while not did_guess_secret:
    attempts += 1
    print(f"This is attempt number {attempts}")
    guess = int(input(f"Guess the secret number (between {minimum} and {maximum}): "))
    did_guess_secret = guess == secret

    if did_guess_secret:
        print(f"You guessed it - congratulations! It's number {secret}.")
        write_scores_to_file()
        break

    if guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

print("End")

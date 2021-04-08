secret = 22

for x in range(5):
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break

    print("Sorry, your guess is not correct... The secret number is not " + str(guess))


# secret = 22
# guess = None

# did_guess_secret = False

# while not did_guess_secret: # While True
#   # Do all this
#    guess = int(input("Guess the secret number (between 1 and 30): "))
#    did_guess_secret = guess == secret
#
#    if did_guess_secret:
#        print("You guessed it - congratulations! It's number 22.")
#    else:
#        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

# print("End")


__author__ = 'Stuart Glassett'

# Write a program to guess a number in a given range in at most 1 + log2n

# Print welcome message
print("Welcome to the guessing game! In this game, you think of a number, 1 to n, and I will try to guess it."
      "After each guess, enter 'h' if my guess is too high, 'l' if it is too low, or 'c' if I am correct.")

# Initialize game values
newgame = True
guess_total = 0
number_games = 0

try:
    upper_limit = int(input("Please enter a number n: "))

    while newgame:

        number_games += 1
        guesses = 0
        upper_bound = upper_limit
        lower_bound = 1

        # Binary search should give us 1 + log2(n)
        correct = False
        while correct is False:
            guesses += 1

            if upper_bound == lower_bound:
                print("Your number is %d." % upper_bound)
                correct = True
            else:
                mid = (upper_bound - lower_bound) // 2 + lower_bound

                guess = input("%d? " % mid)

                # If the guess is correct, stop, otherwise shift the bound to either side of the guess
                if guess == 'c':
                    correct = True
                elif guess == 'h':
                    upper_bound = mid - 1
                elif guess == 'l':
                    lower_bound = mid + 1
                else:
                    # Don't penalize the computer if the user enters an invalid response
                    print("Not a valid response, try again")
                    guesses -= 1

        # Print results
        guess_total = guess_total + guesses
        print("It took %d guesses to guess your number." % guesses)
        print("This resulted in an average of %.3g guesses per game for %d game(s)." % ((guess_total / number_games), number_games))

        a = input("Would you like to play again? (y/n): ")
        if a.lower() != "y":
            newgame = False

except ValueError:
    print("You didn't provide an integer, please try again")

print("Thank you for playing!")

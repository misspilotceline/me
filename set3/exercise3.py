"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def check_bounds(guess, lower_bound, upper_bound):
    if guess < lower_bound or guess > upper_bound:
        print("Oops! Your guess is outside the bounds. Try again.")
        return False
    return True

def play_guessing_game(lower_bound, upper_bound):
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        guess = get_integer_input("Make a guess: ")
        attempts += 1

        if not check_bounds(guess, lower_bound, upper_bound):
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            return "You got it!"

def advancedGuessingGame():
    print("Welcome to the Advanced Guessing Game!")
    lower_bound = get_integer_input("Enter the lower bound: ")
    upper_bound = get_integer_input("Enter the upper bound: ")

    if lower_bound >= upper_bound:
        print( "The lower bound should be smaller than the upper bound. Please try again. ")

    return play_guessing_game(lower_bound, upper_bound)
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """


    # the tests are looking for the exact string "You got it!". Don't modify that!
if __name__ == "__main__":
    print(advancedGuessingGame())

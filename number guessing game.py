# number guessing game
import random
import itertools

difficulty = int(input("what range of numbers would you like? 1 to: "))
number = random.randint(1,difficulty)
moves = 0

for _ in itertools.count():
    guess = input(f"\nguess a number (1 to {difficulty}): ")
    moves += 1
    
    if number == int(guess):
        print(f"\nyou guessed right in {moves} move(s)!")
        difficulty = int(input("\nwhich number range would you like now? 1 to: "))
        number = random.randint(1,difficulty)
        moves = 0
        continue

    elif number > int(guess):
        print("\nhigher")
        continue

    else:
        print("\nlower")
        continue
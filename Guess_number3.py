import random

# Define the levels, max trials, and hints using lists
levels = [1, 2, 3]
max_trials = [5, 7, 3]
hints = [True, False, False]

def guess_the_number(level):
    score = 0

    if level not in levels:
        print("Invalid level. Please choose 1, 2, or 3.")
        return

    # Get index for the selected level
    index = levels.index(level)

    # Get max trials and hint status
    max_trial = max_trials[index]
    hint = hints[index]
    n = random.randint(1, 100)

    print(f"Level {level}: Guess the number ({max_trial} trials, {'with hints' if hint else 'no hints'})")

    for i in range(max_trial):
        num = int(input("Guess a number: "))
        if num == n:
            print("Wonderful, you got the number!")
            score += 50 * level  # Increase points based on level
            break
        elif hint:
            if num < n:
                print("Your guess is lower than the number. Try again.")
            else:
                print("Your guess is higher than the number. Try again.")
        else:
            print("Wrong guess, try again.")
        
        score -= 4
    else:
        print(f"You lost. The number was {n}.")

    print(f"Your score for Level {level}: {score}")
# Example usage:
guess_the_number(1)  # Call for Level 1
#guess_the_number(2)  # Call for Level 2
#guess_the_number(3)  # Call for Level 3
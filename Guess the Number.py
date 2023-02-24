import random

# Generate random number between 1 and 50
number = random.randint(1, 50)

# Initialize guess count to 0
guesses = 0

# Loop until user guesses the correct number
while True:
    # Ask user for guess
    guess = int(input("Guess the number (between 1 and 50): "))
    guesses += 1

    # Check if guess is correct
    if guess == number:
        print("Congratulations, you guessed the number in", guesses, "guesses!")
        break

    # Give hint and continue looping
    elif guess < number:
        print("The number is higher. Try again.")
    else:
        print("The number is lower. Try again.")

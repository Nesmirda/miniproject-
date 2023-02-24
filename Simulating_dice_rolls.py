import random

# Define the number of rolls
num_rolls = 100
# The fewer the number of dice throws, the further the probability of each page
# the more the number of dice throws the same probability of each side

# Initialize the count for each number
count = [0, 0, 0, 0, 0, 0]

# Simulate the rolls
for i in range(num_rolls):
    roll = random.randint(1, 6)
    count[roll - 1] += 1

# Calculate the probabilities
probabilities = [c / num_rolls for c in count]

# Print the result
for i in range(6):
    print(f"The probability of getting {i + 1} is {probabilities[i]:.2f}")

import random
import numpy as np

# Define the number of coin flips
num_flips = 1000
# the more spins the probability of both coins being equal
# as few rotations of the probability are not compared to each other very far from the predictions

# Initialize the count for heads and tails
count_heads = 0
count_tails = 0

# Simulate the coin flips
for i in range(num_flips):
    flip = random.choice(['H', 'T'])
    if flip == 'H':
        count_heads += 1
    else:
        count_tails += 1

# Calculate the probabilities
prob_heads = count_heads / num_flips
prob_tails = count_tails / num_flips

# Print the result
print(f"The probability of getting heads is {prob_heads:.2f}")
print(f"The probability of getting tails is {prob_tails:.2f}")

# HOMEWORK 5 LIST


# LIST:
# Create a list of 50 random numbers between 100 and 500
# Convert the list to a set to get unique numbers
# Count the number of unique numbers
# Print the results

# START

import random

random_numbers = [random.randint(100, 500) for _ in range(50)];

unique_numbers = set(random_numbers);

unique_count = len(unique_numbers);

print("Random numbers:", random_numbers);
print("Number of unique numbers:", unique_count);

# END
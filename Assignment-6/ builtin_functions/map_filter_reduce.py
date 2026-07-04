from functools import reduce

numbers = [10, 20, 30, 40]

# Find the number of elements
print("Length:", len(numbers))

# Find the sum of all elements
print("Sum:", sum(numbers))

# Find the smallest element
print("Minimum:", min(numbers))

# Find the largest element
print("Maximum:", max(numbers))

# Multiply every element by 2
mapped = list(map(lambda x: x * 2, numbers))
print("Map:", mapped)

# Keep only numbers greater than 20
filtered = list(filter(lambda x: x > 20, numbers))
print("Filter:", filtered)

# Add all numbers together
total = reduce(lambda x, y: x + y, numbers)
print("Reduce:", total)

# Print index and value together
for index, value in enumerate(numbers):
    print(index, value)

# Combine two lists
names = ["Alice", "Bob", "Charlie", "David"]
combined = list(zip(names, numbers))
print("Zip:", combined)

# Sort in descending order
print("Sorted:", sorted(numbers, reverse=True))

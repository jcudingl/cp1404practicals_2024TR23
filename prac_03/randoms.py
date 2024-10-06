import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# 5
# 5, 20

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# 5
# 3, 9
# No, 4 is not an odd between 3 and 9

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# 3.594445792566376
# 2.5, close to 3.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))

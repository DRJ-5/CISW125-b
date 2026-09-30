# Intro to Programming
# Debug Exercise 2

# Let's figure out if a number is greater than 5 and less than 10.
# This has two parts; read the comments and don't be afraid to
# contact me on Canvas or email if you have questions.


num= int(input("Enter a whole number. >"))

# Part 1: Discover why this condition doesn't work and fix it.
# Part 2: (Don't do this until part 1 is done)
#         We're testing the same variable twice, to make sure it falls
#         between a range of values. Rewrite the condition to make this simpler.
if num > 5 and num < 10:
    print(f"{num} is less than 10, but greater than 5.")
else:
    print(f"{num} falls outside the bounds we're looking for.")

# integers 5 and 10 has quotation marks on them making them appear as not integers to the program
#changed variable name to just num 
#
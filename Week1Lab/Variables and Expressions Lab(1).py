# CISW 125
# Intro to programming

# Follow the Documentation Policy as it's good practice and will get you used to what you should do for
# your projects and other labs.

# If you're stuck, ask questions. There are no dumb questions.
# ------------------------------------------------------------------------------------------------------
# We're going to play around with variables and expressions today
# The goal is to just test out things and put them to use and possibly
# save the ideas/work for projects down the line.

# Again, the goal is to "play" around and explore. There's no right or wrong to this.
# Just think about input vs output and what we can do with them.
# ------------------------------------------------------------------------------------------------------


# Create some variables, give them a theme. Example: items on a grocery list, games/books/movies you enjoy, etc.
FavAnimal="dog"
food="sandwich"
movies="The Avengers"

# Then print your variables.
print(f"Joeys {FavAnimal} was sitting on his couch while eating a {food} watching {movies}")
# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.
FavAnimal="Tiger"
food="burger"
movies="Spider-Man"
print(f"Joeys {FavAnimal} was sitting on his couch while eating a {food} watching {movies}")
# After you've done this, try to print your variables in string using f-strings.
print(f"In the movie {movies} the main characters pet {FavAnimal} stole a {food} from a pedestrian on the street")

# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
# Store the results of your expressions in a variable and then print the outcome
total1=5*732
total2=10/2
total3=10-5
total4=72+54
print(total1)
print(total2)
print(total3)
print(total4)
total6=total3+total1
print(total6)
# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp


# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.
fname="Daniel"
lname="Rodriguez"
print(f"Hello nice to meet you my name is {fname} {lname} ")
# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)


# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.
f=90
c=32
print(f"if it is {f} degrees Fahrenheit then it is {c} degrees Celsius")
# Upload this to Canvas under the Variable and Expressions Lab assignment.
sum=c*1.8+32
print(sum)
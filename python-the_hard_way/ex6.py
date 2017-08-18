# Sets variable to 10
types_of_people = 10
#sets variable and uses f-string to call the variable that has the # of ppl in it.
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
# The {} is for placing the format that is called in the next line. it calls hilarious and places it's value there
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)

# Creates a variable with a string containing a bunch of curly brackets
formatter = "{} {} {} {}"

#this takes the variable formatter and fills in the valcues in the format function in order
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear",
))


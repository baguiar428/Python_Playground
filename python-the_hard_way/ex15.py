# This imports argv from sys - so that I can use argv to pass parameters to the command
from sys import argv

#This is where i set the variables for the arguments
script, filename = argv

#This opens the filename set as the second paramter to this command and sets it as txt variable
txt = open(filename)

#This uses an f-string to confirm the filename you set
print(f"Here's your file {filename}:")

#This uses a read function/method to se what is in txt variable and then prints it out
print(txt.read())
txt.close()

#Asks you to confirm the filename by inputting it again
print("Type the filename again:")
#Prints out a > prompt and waits for your answer to save to file_again variable
file_again = input('> ')
##file_again = input("Type the filename again\n")

#opens the filename and saves it to text_again variable
txt_again = open(file_again)

#Prints out the contents of the newly assign txt_again file 
print(txt_again.read())
txt_again.close()

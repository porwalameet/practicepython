"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

name = raw_input("Hey, Whats your name?")
age = raw_input("How old are you?")
current_year = 2017
print("Hey %s, you will be turning 100 years in %d") % (name, int(current_year-int(age)+100))

"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

num = int(raw_input("Please enter a number of your choice:"))
if num % 2 == 0:
	print("The number entered in even")
else:
	print("that was an odd number, mate")

if num % 4 ==0:
	print("Wow, its divisible by 4 as well")


from random import randint
import sys

answer = randint(0, 100)

guess = None

try:
	guess = int(input("The computer has chosen an integer between 0 and 100. Can you guess what it is?\nEnter your guess >>> "))

except ValueError as te:
	print("Invalid input! Please only enter integer values. Try again.")

	try:
		guess = int(input("\n \nEnter your guess >>> "))

	except ValueError as te:
		print("Invalid input! Please try again later.")
		sys.exit(1)

	

while(guess != answer):
	if(guess > answer):
		print("Your guess is too high. Try again.\n >>> ")

	elif(guess < answer):
		print("Your guess is too low. Try again.\n >>> ")

	else:
		print("An error has ocurred. Please try to run the program again.")
		sys.exit(1)

	guess = int(input())

if(guess == answer):
	print("Great job! You guessed it!")

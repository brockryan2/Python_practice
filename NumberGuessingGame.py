from random import randint

answer = randint(0, 10)

try:
	guess = int(input("The computer has chosen an integer between 0 and 10. Can you guess what it is?\nEnter your guess >>> "))

except typeError as te:
	

while(guess != answer):
	if(guess > answer):
		print("Your guess is too high. Try again.\n >>> ")

	elif(guess < answer):
		print("Your guess is too low. Try again.\n >>> ")

	guess = int(input())

if(guess == answer):
	print("Great job! You guessed it!")

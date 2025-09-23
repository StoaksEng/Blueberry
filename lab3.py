from random import randint

#initializing default variable states
turns = 12
seq = 4 * [None]
feedback = 4 * [None]
win = False


for i in range(0, 4):
	seq.[i] = randint(1, 6)

for i in range(1, 13):

	try:
		guess = [int(digit) for digit in str(input(f'Input guess #{i}: '))]
	except ValueError:
		print("Invalid input. Please enter a 4-digit number.")

	if len(guess) != 4:
		print("Invalid input. Please enter a 4-digit number.")
		continue

	if guess == seq:
		win = True
		break
	else:
		for i in range(0, 4):
			if guess[i] == seq[i]:
				feedback[i] = '\u25CB'
			elif guess[i] in seq:
				feedback[i] = '\u25CF'
			else:
				feedback[i] = '  '

		print(f'Feedback: {feedback}')
		
		guess = []

if win:
	print(f'You\'ve Won! It took you {i} tries.')
else:
	print(f'You\'ve Lost! The correct sequence is {seq}')
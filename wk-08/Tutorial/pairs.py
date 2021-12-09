positions = (('J', 'Q', 'K', 'J'),
			('A', 'K', 'Q', 'J'),
			('J', 'Q', 'K', 'A'),
			('Q', 'A', 'K', 'A'))

print(' ', 0, 1, 2, 3)
for row in range(4):
	print(row, end='')
	for col in range(4):
		print(' *', end='')
	print()

matched = []
count = 0
while len(matched) < 16:
	coords = []
	for turn in range(1, 3):
		guess = input("Please enter card {} position: ".format(turn))
		row, col = int(guess[0]), int(guess[1])
		while [row, col] in matched or not(0 <= row <= 3) or not(0 <= col <= 3):
			guess = input("Please enter again card {} position: ".format(turn))
			row, col = int(guess[0]), int(guess[1])

		coords += [[row, col]]

		print(' ', 0, 1, 2, 3)
		for row in range(4):
			print(row, end='')
			for col in range(4):
				if [row, col] in coords:
					print(' {}'.format(positions[row][col]), end='')
				elif [row, col] in matched:
					print(' X', end='')
				else:
					print(' *', end='')
			print()

	row0, col0 = coords[0]
	row1, col1 = coords[1]

	if positions[row0][col0] == positions[row1][col1]:
		matched += coords
		print("Well done! You've matched 2 cards")
	else:
		print("Bad luck! You cards didn't match this time")

	print(' ', 0, 1, 2, 3)
	for row in range(4):
		print(row, end='')
		for col in range(4):
			if [row, col] in matched:
				print(' X', end='')
			else:
				print(' *', end='')
		print()

	count += 1

print("Game complete! It took you {} turns.".format(count))

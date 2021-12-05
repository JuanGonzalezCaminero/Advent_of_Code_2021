
import re

file = open("input")

numbers = [int(i) for i in file.readline().split(",")]

boards = [board.split("\n") for board in file.read().lstrip().strip().split("\n\n")]

for board in range(len(boards)):
	for line in range(len(boards[board])):
		boards[board][line] = [int(i) for i in re.split("  | ", boards[board][line].lstrip().strip())]

winner = 0
for n in numbers:
	for board in range(len(boards)):
		for i in range(len(boards[0])):
			for j in range(len(boards[0][0])):
				if boards[board][i][j] == n:
					boards[board][i][j] = -1
					if sum(boards[board][i]) == -5 or sum(list(zip(*boards[board]))[j]) == -5:
						result = sum([i if i>=0 else 0 for i in sum(boards[board], [])])
						print(n * result)
						exit()
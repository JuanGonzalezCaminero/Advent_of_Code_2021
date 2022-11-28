
file = open("input")

octopuses = [[int(i) for i in line.strip()] for line in file.readlines()]

i_max = len(octopuses)
j_max = len(octopuses[0])
total_flashes = 0
iteration = 0

while True:
	iteration+=1

	#Increase all energies by 1
	for i in range(i_max):
		for j in range(j_max):
			octopuses[i][j]+=1

	#Process all flashes until no new ones occur
	iter_flashes = 1
	while iter_flashes != 0:
		iter_flashes = 0

		for i in range(i_max):
			for j in range(j_max):

				if octopuses[i][j] > 9:
					total_flashes+=1
					iter_flashes=1
					octopuses[i][j]=0

					#Update adjacent positions
					for i_aux in range(i-1 if i>0 else i, i+2 if i<i_max-1 else i+1):
						for j_aux in range(j-1 if j>0 else j, j+2 if j<j_max-1 else j+1):
							#Update if it didn't flash during this iteration
							if octopuses[i_aux][j_aux] != 0:
								octopuses[i_aux][j_aux]+=1

	if sum([sum(row) for row in octopuses]) == 0:
		print(iteration)
		break

file = open("input")

data = file.read().strip()
coordinates = data.split("\n\n")[0]
instructions = data.split("\n\n")[1]

dots = [[int(j) for j in i.strip().split(",")] for i in coordinates.split("\n")]
folds = [i.replace("fold along ", "").split("=") for i in instructions.split("\n")]
for i in folds:
	i[1]=int(i[1])

#Do the folds

for fold in folds:
	#Vertical fold
	if fold[0] == "x":
		for d in dots:
			if d[0] > fold[1]:
				d[0] -= 2 * (d[0] - fold[1])
	#Horizontal fold
	if fold[0] == "y":
		for d in dots:
			if d[1] > fold[1]:
				d[1] -= 2 * (d[1] - fold[1])

#Build and display the final result
transparency = [[" " for x in range(max([d[0] for d in dots]) + 1)] for y in range(max(d[1] for d in dots) + 1)]

for d in dots:
	transparency[d[1]][d[0]] = "#"

for i in transparency:
	for j in i:
		print(j, end="")
	print()

from collections import defaultdict

file = open("input")

lines = [[[int(n) for n in j[0].split(",")], [int(n) for n in j[1].split(",")]] for j in [i.split(" -> ") for i in file.readlines()]]

intersections = defaultdict(lambda: 0)

for line in lines:
	dir_i = dir_j = 0
	if line[1][0] != line[0][0]:
		dir_i = 1 if line[1][0]-line[0][0] > 0 else -1
	if line[1][1] != line[0][1]:
		dir_j = 1 if line[1][1]-line[0][1] > 0 else -1
	point = line[0]
	while line[0][0]!=line[1][0] or line[0][1] != line[1][1]:
		intersections[tuple(point)]+=1
		point[0]+=dir_i
		point[1]+=dir_j
	intersections[tuple(line[1])]+=1

print(len([i for i in intersections.values() if i>1]))

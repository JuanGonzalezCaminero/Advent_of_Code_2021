
file = open("input")
heightmap = [[int(j) for j in i.strip()] for i in file.readlines()]
#Add a border of 9s
for i in heightmap:
	i.insert(0, 9)
	i.append(9)
heightmap.insert(0, [9 for i in range(len(heightmap[0]))])
heightmap.append([9 for i in range(len(heightmap[0]))])

result = 0

for i in range(1, len(heightmap)-1):
	for j in range(1, len(heightmap[0])-1):
		height=heightmap[i][j]
		if height<heightmap[i-1][j] and \
			height<heightmap[i+1][j] and \
			height<heightmap[i][j-1] and \
			height<heightmap[i][j+1]:
			result += height+1

print(result)



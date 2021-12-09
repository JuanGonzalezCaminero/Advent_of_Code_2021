
def explore_dfs(i, j, heightmap, basin_map):
	size=0
	if heightmap[i][j+1]!=9 and basin_map[i][j+1]!=1:
		basin_map[i][j+1]=1
		size+=explore_dfs(i, j+1, heightmap, basin_map)
		size+=1

	if heightmap[i+1][j]!=9 and basin_map[i+1][j]!=1:
		basin_map[i+1][j]=1
		size+=explore_dfs(i+1, j, heightmap, basin_map)
		size+=1

	if heightmap[i][j-1]!=9 and basin_map[i][j-1]!=1:
		basin_map[i][j-1]=1
		size+=explore_dfs(i, j-1, heightmap, basin_map)
		size+=1

	if heightmap[i-1][j]!=9 and basin_map[i-1][j]!=1:
		basin_map[i-1][j]=1
		size+=explore_dfs(i-1, j, heightmap, basin_map)
		size+=1

	return(size)

file = open("input")
heightmap = [[int(j) for j in i.strip()] for i in file.readlines()]
#Add a border of 9s
for i in heightmap:
	i.insert(0, 9)
	i.append(9)
heightmap.insert(0, [9 for i in range(len(heightmap[0]))])
heightmap.append([9 for i in range(len(heightmap[0]))])

#This is not strictly necessary (Could just store a list of explored 
#locations) but it may be used to make visualizations
basin_map = [[0 for i in range(len(heightmap[0]))] for j in range(len(heightmap))]

basin_sizes = []

for i in range(1, len(heightmap)-1):
	for j in range(1, len(heightmap[0])-1):
		height=heightmap[i][j]
		if height!=9:
			#Start exploring in a DFS fashion. First move right, then 
			#move down, then left, and finally up:
			size = explore_dfs(i, j, heightmap, basin_map)
			if size!=0:
				basin_sizes.append(size)

basin_sizes.sort()
print(basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3])


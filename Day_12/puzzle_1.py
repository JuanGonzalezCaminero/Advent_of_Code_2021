from collections import defaultdict

file = open("input")

def find_paths(graph, current_node, target_node, unvisited_nodes, current_path, all_paths):
	#Add node to path
	current_path.append(current_node)
	
	#If node is the target, store a copy of the path taken and backtrack
	if current_node == target_node:
		all_paths.append([i for i in current_path])
		unvisited_nodes.append(current_path.pop())
		return

	#Visit all connected unvisited nodes in turn
	for n in graph[current_node]:
		if n in unvisited_nodes or n.isupper():
			if n.islower():
				#Remove the node from the list
				unvisited_nodes.pop(unvisited_nodes.index(n))
			find_paths(graph, n, target_node, unvisited_nodes, current_path, all_paths)

	#Finally, when backtracking, add this node again to the unvisited list, and pop it from the current path
	#(Only if it's a lowercase node)
	current_path.pop()
	if current_node.islower():
		unvisited_nodes.append(current_node)

edges = [line.strip().split("-") for line in file.readlines()]

#Store the graph in a dictionary using an adjacency list representation
graph = defaultdict(list)

for e in edges:
	graph[e[0]].append(e[1])
	graph[e[1]].append(e[0])

#List of all unvisited nodes, adding only lowercase letters
unvisited_nodes = []
for n in graph:
	if n.islower():
		unvisited_nodes.append(n)

print(unvisited_nodes)

#Depth-first search, starting at the 'start' node, whenever the 'end' 
#node is reached, store the path
all_paths=[]
unvisited_nodes.pop(unvisited_nodes.index("start"))
find_paths(graph, "start", "end", unvisited_nodes, [], all_paths)

for i in all_paths:
	print(i)
print(len(all_paths))



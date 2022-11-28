
from collections import defaultdict

file = open("input")

def find_paths(graph, current_node, target_node, unvisited_nodes, current_path, all_paths, second_visit):

	#Add node to path
	current_path.append(current_node)

	#If this is the second visit to this node, decrease the counter for all nodes
	# and raise a flag in order to increase it again when backtracking
	#If a node had triggered the second visit previously, do nothing
	if current_node.islower():
		trigger_second_visit = unvisited_nodes[current_node]==0 and not second_visit and current_node!="start"
		if trigger_second_visit:
			second_visit=True
			for i in unvisited_nodes:
				if i != current_node:
					unvisited_nodes[i]-=1
	
	#If node is the target, store a copy of the path taken and backtrack
	if current_node == target_node:
		all_paths.append([i for i in current_path])
		unvisited_nodes[current_path.pop()]+=1
		return

	#Visit all connected unvisited nodes in turn
	for n in graph[current_node]:
		
		if n.isupper() or unvisited_nodes[n]>0:
			if n.islower():
				#Decrease the node's counter
				unvisited_nodes[n]-=1

			find_paths(graph, n, target_node, unvisited_nodes, current_path, all_paths, second_visit)

	#Finally, when backtracking, add this node again to the unvisited list, and pop it from the current path
	#(Only if it's a lowercase node)
	current_path.pop()

	if current_node.islower():
		if trigger_second_visit:
			for i in unvisited_nodes:
				if i != current_node:
					unvisited_nodes[i]+=1
		unvisited_nodes[current_node]+=1

edges = [line.strip().split("-") for line in file.readlines()]

#Store the graph in a dictionary using an adjacency list representation
graph = defaultdict(list)

for e in edges:
	graph[e[0]].append(e[1])
	graph[e[1]].append(e[0])

#Dict of all unvisited nodes, adding only lowercase letters, initially each node can be visited twice
unvisited_nodes = {}
for n in graph:
	if n.islower():
		unvisited_nodes[n] = 2

#Depth-first search, starting at the 'start' node, whenever the 'end' 
#node is reached, store the path
all_paths=[]
unvisited_nodes["start"]=0
find_paths(graph, "start", "end", unvisited_nodes, [], all_paths, False)

print(len(all_paths))




from collections import defaultdict
import math
import heapq
import itertools

#Python's implementation of a Priority Queue doesn't provide a functionality to reduce a task's 
#priority, this implementation is taken from https://docs.python.org/3/library/heapq.html, 
#implementing the queue using a heapq
class PriorityQueue:
	def __init__(self):
		self.pq = []                         # list of entries arranged in a heap
		self.entry_finder = {}               # mapping of tasks to entries
		self.REMOVED = '<removed-task>'      # placeholder for a removed task
		self.counter = itertools.count()     # unique sequence count

	def add_task(self, task, priority=0):
	    'Add a new task or update the priority of an existing task'
	    if task in self.entry_finder:
	        remove_task(task)
	    count = next(self.counter)
	    entry = [priority, count, task]
	    self.entry_finder[task] = entry
	    heapq.heappush(self.pq, entry)

	def remove_task(self, task):
	    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
	    entry = self.entry_finder.pop(task)
	    entry[-1] = self.REMOVED

	def pop_task(self):
	    'Remove and return the lowest priority task. Raise KeyError if empty.'
	    while self.pq:
	        priority, count, task = heapq.heappop(self.pq)
	        if task is not self.REMOVED:
	            del self.entry_finder[task]
	            return task
	    raise KeyError('pop from an empty priority queue')


def dijkstra(start, cavern):
	distance = defaultdict(lambda: float('inf'))
	prev = {}
	unvisited = {}
	queue = PriorityQueue()

	for i in range(len(cavern)):
		for j in range(len(cavern[0])):
			unvisited[(i, j)]=1
	unvisited_count = len(unvisited)

	distance[start] = 0
	queue.add_task(start, priority=0)

	while unvisited_count != 0:
		print("Visited: " + "{:.4f}".format(((len(unvisited)-unvisited_count)/len(unvisited)*100)) + "%", end="\r")

		current = queue.pop_task()

		unvisited[current]=0
		unvisited_count-=1

		neighbors = [
		(current[0]-1 if current[0]-1>0 else current[0], current[1]),
		(current[0]+1 if current[0]+1<len(cavern) else current[0], current[1]),
		(current[0], current[1]-1 if current[1]-1>0 else current[1]),
		(current[0], current[1]+1 if current[1]+1<len(cavern[0]) else current[1])
		]

		for n in neighbors:
			if unvisited[n]==1:
				if distance[current] + cavern[n[0]][n[1]] < distance[n]:
					distance[n] = distance[current] + cavern[n[0]][n[1]]
					prev[n] = current
					queue.add_task(n, priority=distance[n])

	return distance, prev

file = open("input")

cavern = [[int(i) for i in line.strip()] for line in file.readlines()]

#Extend Horizontally
for row in cavern:
	original_row = row[:]
	for i in range(4):
		row+=[(j+i+1)%10 if (j+i+1)%10>j else (j+i+2)%10 for j in original_row]
#Extend Vertically
original_cavern = cavern[:]
for i in range(4):
	for row in original_cavern:
		cavern.append([(j+i+1)%10 if (j+i+1)%10>j else (j+i+2)%10 for j in row])

print("Cavern: " + str(len(cavern)) + " x " + str(len(cavern[0])))

start = (0, 0)
end = (len(cavern)-1, len(cavern[0])-1)

distance, prev = dijkstra(start, cavern)

print()
print(distance[(len(cavern)-1, len(cavern[0])-1)])
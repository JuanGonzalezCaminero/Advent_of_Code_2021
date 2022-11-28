
from collections import defaultdict

file = open("input")

data = file.read().strip().split("\n\n")

polymer = data[0].strip()
rules = defaultdict(int)

for rule in [i.split(" -> ") for i in data[1].strip().split("\n")]:
	rules[rule[0]] = [rule[0][0] + rule[1], rule[1] + rule[0][1]]

pairs = defaultdict(int)

for index in range(len(polymer) - 1):
	pairs[polymer[index] + polymer[index+1]] += 1

steps = 40

count = defaultdict(int)
for pair in pairs:
	count[pair[0]] += pairs[pair]
count[polymer[-1]] += 1

#Compute the resulting pairs in the polymer
#Each pair is destroyed when inserting a new element, creating two new pairs.
#Since the element is inserted between the pair, other pairs are not affected
new_pairs = defaultdict(int)
for i in range(steps):
	for pair in list(pairs.keys()):
		result = rules[pair]
		if pairs[pair]>=1:
			new_pairs[result[0]] += pairs[pair]
			new_pairs[result[1]] += pairs[pair]

			count[result[0][1]] += pairs[pair]

	pairs = new_pairs
	new_pairs = defaultdict(int)

print(max(count.values()) - min(count.values()))
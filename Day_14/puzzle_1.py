from collections import defaultdict

file = open("input")

data = file.read().strip().split("\n\n")

polymer = data[0].strip()
rules = defaultdict(int)

for rule in [i.split(" -> ") for i in data[1].strip().split("\n")]:
	rules[rule[0]] = rule[0][0] + rule[1]

polymer2 = ""

for i in range(10):
	print("Step: " + str(i))

	index = 0
	while index <= len(polymer) - 2:
		pair = polymer[index:index+2]

		if rules[pair] != 0:
			polymer2 += rules[pair]
		else:
			polymer2 += polymer[index]

		index+=1

	polymer2 += polymer[-1]

	tmp = polymer
	polymer = polymer2
	polymer2 = tmp
	polymer2 = ""


most_common = ""
most_common_count = 0
least_common = ""
least_common_count = len(polymer)

for element in set(polymer):
	count = polymer.count(element)
	if count > most_common_count:
		most_common_count = count
		most_common = element
	if count < least_common_count:
		least_common_count = count
		least_common = element

print(len(polymer))
print(most_common_count - least_common_count)



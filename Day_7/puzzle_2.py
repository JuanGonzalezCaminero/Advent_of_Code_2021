
file = open("input")
crabs = [int(i) for i in file.read().split(",")]
most_common = crabs[0]
most_common_count = crabs.count(crabs[0])
for i in set(crabs):
	if(crabs.count(i) > most_common_count):
		most_common_count = crabs.count(i)
		most_common = i
position = most_common #int(round(sum(crabs)/len(crabs), 0))
print(sum([sum(range(1, abs(i-position)+1)) for i in crabs]))

print(min([sum([sum(range(1, abs(i-position)+1)) for i in crabs]) for position in range(min(crabs), max(crabs)+1)]))

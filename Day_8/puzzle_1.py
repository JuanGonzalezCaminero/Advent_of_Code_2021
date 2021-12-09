
file = open("input")
data = [line.strip().split("|") for line in file.readlines()]
patterns = [i[0].strip().split(" ") for i in data]
displays = [i[1].strip().split(" ") for i in data]

number_lengths = []
for d in displays:
	number_lengths += [len(i) for i in d]

unique_numbers = map(lambda a: 1 if a==2 or a==3 or a==4 or a==7 else 0, number_lengths)

print(sum(list(unique_numbers)))

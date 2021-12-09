
file = open("input")
crabs = [int(i) for i in file.read().split(",")]
crabs.sort()
position = crabs[int(len(crabs)/2)]
print(sum([abs(i-position) for i in crabs]))
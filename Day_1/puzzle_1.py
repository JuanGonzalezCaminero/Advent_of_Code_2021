file = open("input")
data = [int(l) for l in file.readlines()];
result = 0
for i in range(1, len(data)):
	if data[i]>data[i-1]:
		result+=1
print(result)

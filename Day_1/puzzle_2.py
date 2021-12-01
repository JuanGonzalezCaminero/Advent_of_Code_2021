file = open("input")
data = [int(l) for l in file.readlines()];
result = 0
for i in range(3, len(data)):
	if sum(data[i-2:i+1])>sum(data[i-3:i]):
		result+=1
print(result)


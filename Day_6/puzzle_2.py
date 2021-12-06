
file = open("input")

data = [int(i) for i in file.read().split(",")]
fish = [data.count(i) for i in range(9)]

for day in range(256):
	new_fish=fish[0]
	fish[:7]=fish[1:7]+[fish[0]]
	fish[6]+=fish[7]
	fish[7]=fish[8]
	fish[8]=new_fish

print(sum(fish))
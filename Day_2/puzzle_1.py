file = open("input")
commands = [[i[0], int(i[1])] for i in [j.strip().split(" ") for j in file.readlines()]]
#[horizontal, vertical]
position=[0,0]

for c in commands:
	if c[0]=="forward":
		position[0]+=c[1]
	elif c[0]=="down":
		position[1]+=c[1]
	elif c[0]=="up":
		position[1]-=c[1]

print(position[0]*position[1])
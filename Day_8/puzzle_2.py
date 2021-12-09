
file = open("input")
data = [line.strip().split("|") for line in file.readlines()]
patterns = [i[0].strip().split(" ") for i in data]
displays = [i[1].strip().split(" ") for i in data]

result = 0
for i in range(len(patterns)):
	code = {}
	#Start with the easy ones:
	unique_numbers = [set(p) for p in patterns[i] if len(p)!=5 and len(p)!=6]
	for p in unique_numbers:
		if(len(p)==2):
			code["".join(sorted(p))]="1"
			one = p
		elif(len(p)==3):
			code["".join(sorted(p))]="7"
			seven = p
		elif(len(p)==4):
			code["".join(sorted(p))]="4"
			four = p
		elif(len(p)==7):
			code["".join(sorted(p))]="8"
			eight = p

	#Six-segment numbers (0, 6, 9)
	#We can compare with other numbers. The union of 9 and 4 is size 4, the 
	#union of 6 and 7 is size 2, the last one is 0
	six_segment_numbers = [set(p) for p in patterns[i] if len(p)==6]

	for p in six_segment_numbers:
		if len(p.intersection(four)) == 4:
			code["".join(sorted(p))]="9"
			nine=p
		elif len(p.intersection(seven)) == 2:
			code["".join(sorted(p))]="6"
			six=p
		else:
			code["".join(sorted(p))]="0"
			zero=p

	#Five-segment numbers (2, 3, 5)
	#3 has a size 2 intersection with 1, 2 a size 4 intersection with 9, and 
	#5 a size 5 intersection with 9
	five_segment_numbers = [set(p) for p in patterns[i] if len(p)==5]

	for p in five_segment_numbers:
		if len(p.intersection(set(one))) == 2:
			code["".join(sorted(p))]="3"
			three=p
		elif len(p.intersection(set(nine))) == 4:
			code["".join(sorted(p))]="2"
			two=p
		else:
			code["".join(sorted(p))]="5"
			five=p

	#Now we know the code, so it's only a matter of decoding the display
	number = ""
	for j in displays[i]:
		number+=code["".join(sorted(j))]

	result+=int(number)

print(result)
	




file = open("input")

incomplete_lines = []

for line in file.readlines():
	illegal_line = 0
	stack = []
	for c in line.strip():
		if c=="(" or c=="["or c=="{" or c=="<":
			stack.append(c)
		elif c==")" and stack[-1]=="(":
			stack.pop(-1)
		elif c=="}" and stack[-1]=="{":
			stack.pop(-1)
		elif c=="]" and stack[-1]=="[":
			stack.pop(-1)
		elif c==">" and stack[-1]=="<":
			stack.pop(-1)
		else:
			#Illegal character
			illegal_line = 1
			break
	if not illegal_line:
		incomplete_lines.append(line)

scores = []
for line in incomplete_lines:
	stack=[]
	for c in line.strip():
		if c=="(" or c=="["or c=="{" or c=="<":
			stack.append(c)
		elif c==")" and stack[-1]=="(":
			stack.pop(-1)
		elif c=="}" and stack[-1]=="{":
			stack.pop(-1)
		elif c=="]" and stack[-1]=="[":
			stack.pop(-1)
		elif c==">" and stack[-1]=="<":
			stack.pop(-1)
	#Whatever remains on the stack is what needs to be closed to complete 
	#the line
	line_score = 0
	for c in stack[::-1]:
		if c=="(":
			line_score = line_score * 5 + 1
		elif c=="[":
			line_score = line_score * 5 + 2
		elif c=="{":
			line_score = line_score * 5 + 3
		elif c=="<":
			line_score = line_score * 5 + 4
	scores.append(line_score)

scores.sort()
print(scores[int(len(scores)/2)])




		
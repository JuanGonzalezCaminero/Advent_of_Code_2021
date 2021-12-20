
file = open("input")

result = 0
for line in file.readlines():
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
			if c==")":
				result += 3
			elif c=="}":
				result += 1197
			elif c=="]":
				result += 57
			elif c==">":
				result += 25137
			break

print(result)




		
file = open("input")
numbers = [i.strip() for i in file.readlines()]

numbers_aux = [i for i in numbers]

for position in range(len(numbers_aux[0])):
	list_0 = [i for i in numbers_aux if i[position] == "0"]
	list_1 = [i for i in numbers_aux if i[position] == "1"]
	if(len(list_0) > len(list_1)):
		numbers_aux = list_0
	else:
		numbers_aux = list_1
		
	if(len(numbers_aux) == 1):
		break

o2_rating = numbers_aux[0]

numbers_aux = [i for i in numbers]

for position in range(len(numbers_aux[0])):
	list_0 = [i for i in numbers_aux if i[position] == "0"]
	list_1 = [i for i in numbers_aux if i[position] == "1"]

	if(len(list_1) < len(list_0)):
		numbers_aux = list_1
	else:
		numbers_aux = list_0

	if(len(numbers_aux) == 1):
		break

co2_rating = numbers_aux[0]

print(int(o2_rating, 2) * int(co2_rating, 2))

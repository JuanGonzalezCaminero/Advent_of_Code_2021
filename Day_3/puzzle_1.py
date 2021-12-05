file = open("input")
numbers = [i.strip() for i in file.readlines()]
gamma_rate = "".join(["0" if position.count("0") > len(numbers)/2 else "1" for position in zip(*numbers)])
epsilon_rate = "".join(["0" if gamma_bit == "1" else "1" for gamma_bit in gamma_rate])
print(int(gamma_rate, 2) * int(epsilon_rate, 2))
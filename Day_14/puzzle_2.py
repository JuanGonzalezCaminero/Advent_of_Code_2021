
from collections import defaultdict

def do_step(polymer, rules, count, rule_counts):
	polymer2 = []

	index = 0
	while index <= len(polymer) - 2:
		if len(polymer[index]) == 1 and len(polymer[index+1]) == 1:
			pair = "".join(polymer[index:index+2])

			if rules[pair] != 0:
				polymer2.append(rules[pair])
				for i in rule_counts[pair]:
					count[i] += rule_counts[pair][i]
			else:
				polymer2.append(polymer[index])
				count[polymer[index]] += 1

		elif len(polymer[index]) == 1:
			polymer2.append(polymer[index])
			count[polymer[index]] += 1

		elif len(polymer[index]) != 1:
			polymer2.append(do_step(polymer[index], rules, count, rule_counts))
			count[polymer2[-1][-1]] -= 1

		index+=1

	polymer2 += polymer[-1]
	count[polymer[-1]]+=1

	polymer = polymer2
	polymer2 = ""

	return polymer

def compute_fastforward_rules(rules, fastforward_steps):
	fastforward_rules = defaultdict(int)

	for pair in rules:
		#Compute what the pair will evolve to in X steps
		p = pair[:]
		p_aux = ""

		for i in range(fastforward_steps):
			#p = do_step(p, rules)

			index = 0
			while index <= len(p) - 2:
				current_pair = p[index:index+2]

				if rules[current_pair] != 0:
					p_aux += rules[current_pair]
				else:
					p_aux += p[index]

				index+=1

			p_aux += p[-1]

			p = p_aux
			p_aux = ""

		#The rule will now replace the pair with it's evolution after X steps
		fastforward_rules[pair] = p

	return fastforward_rules

#############################################################################
#############################################################################

file = open("input")

data = file.read().strip().split("\n\n")

polymer = data[0].strip()
rules = defaultdict(int)

for rule in [i.split(" -> ") for i in data[1].strip().split("\n")]:
	rules[rule[0]] = rule[0][0] + rule[1]

fastforward_steps = 20
recursion_steps = 2

#Compute fast-forward rules, that do several steps in one operation
fastforward_rules = compute_fastforward_rules(rules, fastforward_steps)

#Get the character count for the result of each rule
rule_counts = defaultdict(int)

for i in fastforward_rules:
	rule_counts[i] = defaultdict(int)
	for j in fastforward_rules[i][:-1]:
		rule_counts[i][j] += 1

polymer = list(polymer)
count = defaultdict(int)

#Apply the new rules several times in order to get the final polymer
for i in range(recursion_steps):
	count = defaultdict(int)
	polymer = do_step(polymer, fastforward_rules, count, rule_counts)

print(max(count.values()) - min(count.values()))

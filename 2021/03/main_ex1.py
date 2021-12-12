i = 0
n = 0
calc = []
gamma = ""
epsilon = ""
with open("data.txt", "r") as data_file:
	i = len(data_file.readline())
	print(i)
	for n in range(0, i):
		calc.append("0")

	for line in data_file:
		for n in range(0, i - 1):
			if line[n] == "1":
				calc[n] = int(calc[n]) + 1
			elif line[n] == "0":
				calc[n] = int(calc[n]) - 1

	for n in range(0, i):
		if int(calc[n]) < 0:
			gamma = gamma + "1"
			epsilon = epsilon + "0"
		elif int(calc[n]) > 0:
			gamma = gamma + "0"
			epsilon = epsilon + "1"

print(int(gamma, 2)*int(epsilon, 2))


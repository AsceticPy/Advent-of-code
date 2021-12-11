depth = 0
horizon = 0
aim = 0

with open("data.txt") as data_file:
	for line in data_file:
		full_order = str(line)
		order = full_order.split(" ")[0]
		number_case = full_order.split(" ")[1]
		if order ==  "forward":
			horizon = int(horizon) + int(number_case)
			depth = depth + (int(aim) * int(number_case))
		elif order ==  "down":
			aim = int(aim) + int(number_case)
		elif order ==  "up":
			aim = int(aim) - int(number_case)


print(depth*horizon)
depth = 0
horizon = 0

with open("data.txt") as data_file:
	for line in data_file:
		full_order = str(line)
		order = full_order.split(" ")[0]
		number_case = full_order.split(" ")[1]
		print(order)
		print(number_case)
		if order ==  "forward":
			horizon = int(horizon) + int(number_case)
		elif order ==  "down":
			depth = int(depth) + int(number_case)
		elif order ==  "up":
			depth = int(depth) - int(number_case)


print(depth*horizon)
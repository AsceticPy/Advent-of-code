input: str = ''
with open("data.txt", "r") as data_file:
	input = data_file.readline() 

print(sum([1 if char == '(' else -1 for char in input]))
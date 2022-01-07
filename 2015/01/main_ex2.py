input: str = ''
with open("data.txt", "r") as data_file:
	input = data_file.readline() 

floor = 0
for n in range(len(input)):
    if input[n] == '(':
        floor += 1
    else:
        floor -= 1
        
    if floor == -1:
        print(n + 1)
        break
        
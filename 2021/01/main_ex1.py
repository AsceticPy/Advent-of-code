depth_list = []

with open('data.txt') as datafile:
    for line in datafile:
        depth_list.append(int(line))
last = depth_list[1]
counter = 0
for depth in depth_list:
    if depth > last:
        counter = counter + 1
    last = depth
print(counter)

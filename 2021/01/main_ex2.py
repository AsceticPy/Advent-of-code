depth_list = []

with open('data.txt') as datafile:
    for line in datafile:
        depth_list.append(int(line))
last = depth_list[1]
counter = 0
n = 0
windowsA = 0
windowsB = 0
print(len(depth_list))
for depth in depth_list:
    if n + 3 < len(depth_list):
        windowsA = depth + depth_list[n + 1] + depth_list[n + 2]
        windowsB = depth_list[n + 1] + depth_list[n + 2] + depth_list[n + 3]
        if windowsB > windowsA:
            counter = counter + 1
        n = n + 1
print(counter)

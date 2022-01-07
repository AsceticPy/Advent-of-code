lines = []

def solve(input: str) -> int:
    result = 0
    for line in input:
        l, w, h = int(line.split('x')[0]), int(line.split('x')[1]), int(line.split('x')[2])
        result += ((2 * l * w) + (2 * w * h) + (2 * h * l) + min((l * w), (w * h), (h * l)))

    return result

with open("data.txt", "r") as data_file:
    while True:
        line0 = data_file.readline()
        if not line0:
            break
        lines.append(line0.strip())

print(solve(lines))
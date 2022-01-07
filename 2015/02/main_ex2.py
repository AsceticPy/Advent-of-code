lines = []

def solve(input: str) -> int:
    result = 0
    for line in input:
        l, w, h = int(line.split('x')[0]), int(line.split('x')[1]), int(line.split('x')[2])
        result += min((2 * (l + w)), (2 * (l + h)), (2 * (h + w))) + (l * w * h)

    return result

with open("data.txt", "r") as data_file:
    while True:
        line0 = data_file.readline()
        if not line0:
            break
        lines.append(line0.strip())

print(solve(lines))
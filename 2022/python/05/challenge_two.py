import re
REGEX_DIGITS = re.compile(r"\d+")

def main():
    with open("stacks.txt", "r") as file:
        crates = [[] for n in range(9)]
        for line in file:
            crates.append([])
            current_stacks = 0
            if line != "\n":
                for n in range(0, len(line), 4):
                    if line[n] == "[":
                        crates[current_stacks].insert(0, line[n + 1])
                    current_stacks += 1
    
    with open("data.txt", "r") as file:
        for line in file:
            digits = re.findall(REGEX_DIGITS, line)
            if digits:
                for n in range(int(digits[0])):
                    crates[int(digits[2]) - 1].append(crates[int(digits[1]) - 1][len(crates[int(digits[1]) - 1]) - (int(digits[0]) - n)])
                    crates[int(digits[1]) - 1].pop(len(crates[int(digits[1]) - 1]) - (int(digits[0]) - n))

    print(''.join([crates[n][-1] for n in range(9)]))
    

if __name__ == "__main__":
    main()

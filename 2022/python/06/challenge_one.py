def main():
    with open("data.txt", "r") as file:
        for line in file:
            key = []
            for position, char in enumerate(line):
                key.append(char)
                if len(key) == 4:
                    res = []
                    [res.append(x) for x in key if x not in res]
                    if res == key:
                        print(position + 1)
                    else:
                        key.pop(0)

if __name__ == "__main__":
    main()

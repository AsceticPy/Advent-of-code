def main():
    with open("data.txt", "r") as file:
        for line in file:
            key = []
            position = 0
            unique = False
            for char in line:
                key.append(char)
                position += 1
                if len(key) == 4:
                    res = []
                    [res.append(x) for x in key if x not in res]
                    if res == key:
                        print(position)
                    else:
                        key.pop(0)

if __name__ == "__main__":
    main()

def main():
    with open("test.txt", "r") as file:
        counter = 0
        for line in file:
            data = line.strip()
            part_one, part_two = data.split(",")

            x1, y1 = part_one.split("-")
            x2, y2 = part_two.split("-")

            range_one = [n for n in range(int(x1), int(y1) + 1)]
            range_two = [n for n in range(int(x2), int(y2) + 1)]

            if any([True for n in range_one if n in range_two]):
                counter += 1
                print("1: " + x1, y1, x2, y2)


    print(counter)

if __name__ == "__main__":
    main()

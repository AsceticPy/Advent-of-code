def main():
    with open("data.txt", "r") as file:
        counter = 0
        for line in file:
            data = line.strip()
            part_one, part_two = data.split(",")

            x1, y1 = part_one.split("-")
            x2, y2 = part_two.split("-")

            if int(x1) <= int(x2) and int(y1) >= int(y2):
                counter += 1
                print(x1, y1, x2, y2)
            
            elif int(x2) <= int(x1) and int(y2) >= int(y1):
                counter += 1
                print("2 : " + x1, y1, x2, y2)

    print(counter)

if __name__ == "__main__":
    main()

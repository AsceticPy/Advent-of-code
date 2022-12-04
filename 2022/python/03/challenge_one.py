import string
alphabet = {string.ascii_lowercase[i]: i + 1 for i in range(len(string.ascii_lowercase))}
alphabet_upper = {string.ascii_uppercase[i]: i + 27 for i in range(len(string.ascii_uppercase))}


def main():
    with open ("data.txt", "r") as file:
        score = 0
        for line in file:
            letter_find = []
            data = line.strip()
            part = int(len(data) / 2)
            part_one, part_two = line[:part], line[part:]
            for n in range(part):
                for i in range(part):
                    if part_one[n] == part_two[i] and not part_one[n] in letter_find:
                        if part_one[n] in alphabet.keys():
                            score += alphabet[part_one[n]]
                            letter_find.append(part_one[n])
                        elif part_one[n] in alphabet_upper.keys():
                            score += alphabet_upper[part_one[n]]
                            letter_find.append(part_one[n])

            
        print(score)



if __name__ == "__main__":
    main()

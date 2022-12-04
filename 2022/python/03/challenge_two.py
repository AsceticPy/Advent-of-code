import string
alphabet = {string.ascii_lowercase[i]: i + 1 for i in range(len(string.ascii_lowercase))}
alphabet_upper = {string.ascii_uppercase[i]: i + 27 for i in range(len(string.ascii_uppercase))}


print(alphabet, alphabet_upper)

def main():
    with open ("data.txt", "r") as file:
        score = 0
        lines = []
        letter_find = []
        for line in file:
            lines.append(line.strip())
        print(lines)
        for t in range(0, len(lines), 3):
            letter_find = []
            badge = ""
            part_one, part_two, part_three = lines[t], lines[t + 1], lines[t + 2]
            for n in range(len(part_one)):
                for i in range(len(part_two)):
                    for z in range(len((part_three))):
                        if part_one[n] == part_two[i] and part_two[i] == part_three[z] and not badge in letter_find:
                            badge = part_one[n]
                            letter_find.append(badge)
                            print(badge)
                            if badge in alphabet.keys():
                                score += alphabet[badge]
                            else:
                                score += alphabet_upper[badge]

            
        print(score)



if __name__ == "__main__":
    main()

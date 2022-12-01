with open('data.txt', 'r') as file:
    elf= [0]
    elf_num: int = 0
    elf_cal = 0
    for line in file:
        if line == "\n":
            elf[elf_num] = elf_cal
            elf_cal = 0
            elf.append(0)
            elf_num += 1
        else:
            elf_cal += int(line)
    
    print(f"The higest cal carying by one Elf is {max(elf)}")
        

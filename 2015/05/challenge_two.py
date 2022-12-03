import re

REGEX_PAIR = re.compile(r"([a-z]{2}).*\1")
REGEX_REPEAT = re.compile(r"([a-z]).\1{1}")

def is_nice_string(input: str):
    if re.search(REGEX_PAIR, input) and re.search(REGEX_REPEAT, input):
            return True
    return False
    
def main():
    counter_nice_string = 0
    with open("data.txt", "r") as file:
        for line in file:
            if is_nice_string(line):
                counter_nice_string += 1
    print(counter_nice_string)

    

if __name__ == "__main__":
    main()

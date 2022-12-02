from hashlib import md5
import encodings

SECRET_KEY = "bgvyzdsv" #Puzzle input

def main():
    increment = 0
    while True:
        
        KEY = f"{SECRET_KEY}{str(increment)}"
        KEY = bytes(KEY, encoding="utf8")
        
        hash_result = md5(KEY).hexdigest()
        if hash_result[:6] == "000000":
            print(increment, KEY, hash_result)
            break
        else:
            increment += 1

if __name__ == "__main__":
    main()
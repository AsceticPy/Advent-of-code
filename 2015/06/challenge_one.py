MATRICE_LENGTH = 1000


def ligth_rect(x1: int, x2: int, y1: int, y2: int):
    ligths = []
    for m in range(x1, x2 + 1):
        for n in range(y1, y2 + 1):
            ligths.append((m, n))
    return ligths

def turn_on(matrice, ligth):
    for x, y in ligth:
        matrice[x][y] = 1
    

def turn_off(matrice, ligth):
    for x, y in ligth:
        matrice[x][y] = 0

def toggle(matrice, ligth):
    for x, y in ligth:
        if matrice[x][y] == 1:
            matrice[x][y] = 0
        else:
            matrice[x][y] = 1

def count_ligth_on(matrice):
    counter = 0
    for m in range(MATRICE_LENGTH):
        for n in range(MATRICE_LENGTH):
            if matrice[m][n] == 1:
                counter += 1
    return counter


def main():
    with open("data.txt", "r") as file:
        number_ligth = 0
        matrix = [[0 for n in range(MATRICE_LENGTH)] for z in range(MATRICE_LENGTH)]
        for line in file:
            if 'toggle' in line:
                data_split = line.split(" ")
                top_corner, bottom_corner = data_split[1], data_split[3]
                x1, y1 = int(top_corner.split(",")[0]), int(top_corner.split(",")[1])
                x2, y2 = int(bottom_corner.split(",")[0]), int(bottom_corner.split(",")[1])
                number_ligth += (x2 - x1) * (y2 - y1)
                toggle(matrix, ligth_rect(x1, x2, y1, y2))
            elif 'on' in line:
                data_split = line.split(" ")
                top_corner, bottom_corner = data_split[2], data_split[4]
                x1, y1 = int(top_corner.split(",")[0]), int(top_corner.split(",")[1])
                x2, y2 = int(bottom_corner.split(",")[0]), int(bottom_corner.split(",")[1])
                number_ligth += (x2 - x1) * (y2 - y1)
                turn_on(matrix, ligth_rect(x1, x2, y1, y2))
            else:
                data_split = line.split(" ")
                top_corner, bottom_corner = data_split[2], data_split[4]
                x1, y1 = int(top_corner.split(",")[0]), int(top_corner.split(",")[1])
                x2, y2 = int(bottom_corner.split(",")[0]), int(bottom_corner.split(",")[1])
                number_ligth += (x2 - x1) * (y2 - y1)
                turn_off(matrix, ligth_rect(x1, x2, y1, y2))

        print(count_ligth_on(matrix))
        

if __name__ == "__main__":
    main()

smoke_flows = []

def solve(matrice: int) -> int:
   counter = 0
   l_matrice = len(matrice) - 1
   for n in range(len(matrice)):
      long_matrice = len(matrice[n]) - 1
      for i in range(len(matrice[n])):
         list_check = []
         if n - 1 < 0 and i - 1 < 0:
            list_check.extend([matrice[n][i], matrice[n + 1][i], matrice[n][i + 1]])
            if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               counter += matrice[n][i] + 1
         elif n - 1 < 0 and i + 1 > long_matrice:
            list_check.extend([matrice[n][i], matrice[n + 1][i], matrice[n][i - 1]])
            if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               counter += matrice[n][i] + 1
         elif n + 1 > l_matrice and i - 1 < 0:
            list_check.extend([matrice[n][i], matrice[n - 1][i], matrice[n][i + 1]])
            if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               counter += matrice[n][i] + 1
         elif n + 1 > l_matrice and i + 1 > long_matrice:
            list_check.extend([matrice[n][i], matrice[n - 1][i], matrice[n][i - 1]])
            if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               counter += matrice[n][i] + 1
         elif n - 1 < 0:
            list_check.extend([matrice[n][i], matrice[n][i - 1], matrice[n][i + 1], matrice[n + 1][i]])
            if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               counter += matrice[n][i] + 1
         elif n + 1 > l_matrice:
            list_check.extend([matrice[n][i], matrice[n][i - 1], matrice[n][i + 1], matrice[n - 1][i]])
            if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               counter += matrice[n][i] + 1
         elif i - 1 < 0:
            list_check.extend([matrice[n][i], matrice[n - 1][i], matrice[n + 1][i], matrice[n][i + 1]])
            if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               counter += matrice[n][i] + 1
         elif i + 1 > long_matrice:
            list_check.extend([matrice[n][i], matrice[n - 1][i], matrice[n + 1][i], matrice[n][i - 1]])
            if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               counter += matrice[n][i] + 1
         else:
            list_check.extend([matrice[n][i], matrice[n - 1][i], matrice[n + 1][i], matrice[n][i - 1], matrice[n][i + 1]])
            if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               counter += matrice[n][i] + 1
   return counter
   
with open("data.txt", "r") as data_file:
   while True:
      line = data_file.readline()
      if not line:
         break
      smoke_flows.append(list(map(int,line.strip())))

print(solve(smoke_flows))
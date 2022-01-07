from dataclasses import dataclass

smoke_flows = []

@dataclass
class Point:
   coordX: int
   coordY: int
   value: int
   explore:bool = False

def avaible_positions(matrice:int, coordX: int, coordY: int, switch: bool = False) -> int:
   positions = [[coordX - 1, coordY],[coordX + 1, coordY],[coordX, coordY - 1],[coordX, coordY + 1]]
   positions_to_test = [matrice[coordY][coordX]]
   n_error = 0
   for position in positions:
      try:
         if position[0] < 0 or position[1] < 0:
            ERROR = 1 / 0
         if not switch:
            positions_to_test.append(matrice[position[1]][position[0]])
         else:
            if matrice[position[1]][position[0]] < 9:
               positions_to_test.append([position[1], position[0]])
      except:
         n_error += 1
         
   if switch:
      positions_to_test.pop(0)
      
   return positions_to_test
   
def discover_low_points(matrice: int) -> Point:
   points:Point = []
   for n in range(len(matrice)):
      for i in range(len(matrice[n])):
         list_check = avaible_positions(matrice, i, n)
         if matrice[n][i] == min(list_check) and not len(set(list_check)) == 1:
               points.append(Point(i, n, matrice[n][i]))
   return points

def discover_cave() -> int:
   matrice: Point = discover_low_points(smoke_flows)
   caves: int = []
   
   for point in matrice:
      cave: Point = [point]
      while not all(c.explore for c in cave):
         for pt in cave:
            if not pt.explore:
               check_position = avaible_positions(smoke_flows, pt.coordX, pt.coordY, True)
               pt.explore = True
               for pos in check_position:
                  if not any(True for p in cave if p.coordX == pos[1] and p.coordY == pos[0]):
                     cave.append(Point(pos[1], pos[0], smoke_flows[pos[0]][pos[1]]))
      caves.append(len(cave))
   caves.sort(reverse=True)
   return caves[0] * caves[1] * caves[2]
      
with open("data.txt", "r") as data_file:
   while True:
      line = data_file.readline()
      if not line:
         break
      smoke_flows.append(list(map(int,line.strip())))

print(discover_cave())
global_counter = 0

with open("data.txt", "r") as datafile:
   while True:
      line = datafile.readline()
      if not line:
         break
      line = line.strip().split(" | ")[1].split()
      global_counter += sum(1 for i in range(len(line)) if len(line[i]) == 2 or len(line[i]) == 3 or len(line[i]) == 4 or len(line[i]) == 7)
      
print(global_counter)

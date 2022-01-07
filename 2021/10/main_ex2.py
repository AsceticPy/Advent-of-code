import math 

lines: str = []
list_open_char: str = ['(', '[', '{', '<']
list_close_char: str = [')', ']', '}', '>']
char_value: int = [1, 2, 3, 4]


def complet_line(input0: str) -> int:
   input_open_char: str = []
   
   for char in input0:
      if char in list_open_char:
         input_open_char.append(char)
      elif char in list_close_char:
         input_open_char.pop()
         
   value:int = 0
   
   input_open_char = [char for char in reversed(input_open_char)]
   for n in range(len(input_open_char)):
      value = (value * 5) + char_value[[i for i in range(len(list_open_char)) if list_open_char[i] == input_open_char[n]][0]]
            
   return value
         
def solve(input0: str) -> int:
   input_char_open: str = []
   
   for n in range(len(input0)):
      if input0[n] in list_open_char:
         input_char_open.append(input0[n])
      if input0[n] in list_close_char:
         list_index = [i for i in range(len(list_close_char)) if list_close_char[i] == input0[n]]
         close_char, open_char = list_close_char[list_index[0]], list_open_char[list_index[0]]
         if input_char_open[-1] != open_char[0]:
            return char_value[list_index[0]]
         else:
            input_char_open.pop()
            
   return 0
   
with open("data.txt", "r") as data_file:
   while True:
      line = data_file.readline()
      if not line:
         break
      lines.append(line.strip())

result_of_line: int = []

for line in lines:
   if solve(line) == 0:
      result_of_line.append(complet_line(line))
      
result_of_line = sorted(result_of_line)
print(result_of_line[len(result_of_line) // 2])
      
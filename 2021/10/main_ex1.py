lines: str = []
list_open_char: str = ['(', '[', '{', '<']
list_close_char: str = [')', ']', '}', '>']
char_value: int = [3, 57, 1197, 25137]

   
def solve(input0: str) -> int:
   
   input_char_open = []
   
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


print(sum([solve(line) for line in lines]))
      
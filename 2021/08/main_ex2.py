"""
SEGMENTS OF DIGITS :
   
 000
5   1
5   1
 666
4   2
4   2
 333
 
"""

def solve_line(numbers: str):
   segments = {0:'x', 1:'x', 2:'x', 3:'x', 4:'x', 5:'x', 6:'x'}
   print(numbers)
   while any(segments[t] == 'x' for t in range(len(segments))):
      one = [number for number in numbers if len(number) == 2]
      four = [number for number in numbers if len(number) == 4]
      seven = [number for number in numbers if len(number) == 3]
      eight = [number for number in numbers if len(number) == 7]
      five_long = [number for number in numbers if len(number) == 5]
      six_long = [number for number in numbers if len(number) == 6]
      
      one_flag = 0
      two_flag = 0
      
      for six in six_long:
         if one[0][0] in six:
            print('one')
            one_flag += 1
         if one[0][1] in six:
            print('two')
            two_flag += 1

      if one_flag < two_flag:
         segments[1] = one[0][0]
         segments[2] = one[0][1]
      else:
         segments[1] = one[0][1]
         segments[2] = one[0][0]
         
      segments[0] = [char for char in seven[0] if char != segments[1] and char != segments[2]][0]
      while segments[4] == 'x' or segments[5] == 'x':
         for five in five_long:
            for char in five:            
               flag_five = True
               flag_four = True
               for f in five_long:
                  if segments[4] == 'x':
                     if (char in f or char in four[0]) and f != five:
                        flag_five = False
                        break
                  else:
                     if (char in f or char not in four[0]) and f != five:
                        flag_four = False
                        break
               if segments[4] == 'x':
                  if flag_five:
                     segments[4] = char
               else: 
                  if flag_four and segments[5] == 'x':
                     segments[5] = char
                     segments[6] = [char for char in four[0] if char != segments[1] and char != segments[2] and char != segments[5]][0]
                     segments[3] = [char for char in eight[0] if char != segments[0] and char != segments[1] and char != segments[2] and char != segments[4] and char != segments[5] and char != segments[6]][0]    
         
      
   model_digits = [
     [segments[0], segments[1], segments[2], segments[3], segments[4], segments[5]]
   , [segments[1], segments[2]]
   , [segments[0], segments[1], segments[3], segments[4], segments[6]]
   , [segments[0], segments[1], segments[2], segments[3], segments[6]]
   , [segments[1], segments[2], segments[5], segments[6]]
   , [segments[0], segments[2], segments[3], segments[5], segments[6]]
   , [segments[0], segments[2], segments[3], segments[4], segments[5], segments[6]]
   , [segments[0], segments[1], segments[2]]
   , [segments[0], segments[1], segments[2], segments[3], segments[4], segments[5], segments[6]]
   , [segments[0], segments[1], segments[2], segments[3], segments[5], segments[6]]
   ]
   return model_digits

def unique_digit(model_digits, list_digits, input_string) -> str:
   result = []
   for inpt in input_string:
      inpt_to_find = sorted(inpt)
      for n in range(len(list_digits)):
         if inpt_to_find == sorted(model_digits[list_digits[n]]):
            result.append(list_digits[n])
   if len(result) == 3:
      print(result)
      print(input_string)
   return result

list_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
global_counter = 0

with open("data.txt", "r") as datafile:
   while True:
      line = datafile.readline()
      if not line:
         break
      line0, line1 = line.strip().split(" | ")[0].split(), line.strip().split(" | ")[1].split()
      global_counter += int(''.join(list(map(str,unique_digit(solve_line(line0), list_digits, line1)))))
      
print(global_counter)
   
from typing import Optional
"""Reading information inspired by the solution of @hurryabit, 
	thank's to you i learn so much by reading your code
	Github : https://github.com/hurryabit/
	His solution : https://github.com/hurryabit/adventofcode-2021/blob/main/python/day04a.py """

Grille = list[list[Optional[int]]]

class grille_bingo(object):
	"""docstring for grille_bingo"""


	def __init__(self, number: Grille, sum_grille: int, winner: bool, id: int):
		self.number = number
		self.sum_grille = sum_grille
		self.winner = winner
		self.id = id

	def find_number(self, num: int):
		i = 0
		for line in self.number:
			if num in line:
				self.number[i] = [" " if item == num else item for item in self.number[i]]
				self.sum_grille = self.sum_grille - num
			i = i + 1

	def is_win(self) -> bool:
		def check_row(rows: Grille):
			return any(all(cell == " " for cell in row) for row in rows) or any(all(cell == " " for cell in row) for row in zip(*rows))

		i = check_row(self.number)
		if i:
			return True



i = 1

with open("data.txt", "r") as data_file:
	numbers = list(map(int, data_file.readline().strip().split(",")))
	boards:grille_bingo = []

	while True:
		line = data_file.readline()
		if not line:
			break

		board: Grille = []

		for _ in range(5):
			board.append(list(map(int,data_file.readline().strip().split())))

		boards.append(grille_bingo(board, sum([sum(i) for i in zip(*board)]), False, i))
		i = i + 1

	for num in numbers:
		for b in boards:
			if b.winner == False:
				b.find_number(num)
				if b.is_win():
					b.winner = True
					result = b.sum_grille*num
	print("The score of the last winner board is : ", result)



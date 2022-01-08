from dataclasses import dataclass


flash_tot: int = 0
lines: int = []

class Octopus:
	def __init__(self, x: int, y: int, value: int, flash: bool):
		self.x = x
		self.y = y
		self.flash = flash
		self._value = value


	@property
	def value(self):
		return int(self._value)

	@value.setter
	def value(self, v):
		if not self.flash:
			self._value = v


	def Flash(self):
		if not self.flash:
			global flash_tot
			flash_tot += 1
			self._value = 0
			self.flash = True
			positions = [[self.x - 1, self.y], [self.x + 1, self.y], [self.x , self.y - 1], [self.x, self.y + 1]
							, [self.x - 1, self.y - 1], [self.x + 1, self.y - 1], [self.x + 1, self.y + 1], [self.x - 1, self.y + 1]]

			for position in positions:
				if is_valid(position[0], position[1]):
					octopus[position[0]][position[1]].value += 1
					if octopus[position[0]][position[1]].value > 9:
						octopus[position[0]][position[1]].Flash()


def is_valid(x: int, y: int) -> bool:
		return (0 <= x < len(octopus)) and (0 <= y < len(octopus[0]))

def step():
	for n in range(len(octopus)):
		for i in range(len(octopus[0])):
			octopus[i][n].value += 1


	for n in range(len(octopus)):
		for i in range(len(octopus[0])):
			if octopus[i][n].value > 9:
				octopus[i][n].Flash()

	for n in range(len(octopus)):
		for i in range(len(octopus[0])):
			octopus[i][n].flash = False


octopus:Octopus = []

with open('example.txt', 'r') as data_file:
	lines = [line.strip() for line in data_file]
	for i in range(len(lines)):
		octopus.append([])
		for n in range(len(lines[i])):
			octopus[i].append(Octopus(n, i, lines[i][n], False))

for i in range(10):
	step()

for n in range(len(octopus)):
	for i in range(len(octopus[0])):
		print(octopus[n][i].value, end=',')
	print("\n")
print(flash_tot)
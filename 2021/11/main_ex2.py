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
		global flash_tot
		flash_tot += 1
		self._value = 0
		self.flash = True
		positions = [
					[self.x - 1, self.y], [self.x + 1, self.y], 
					[self.x , self.y - 1], [self.x, self.y + 1], 
					[self.x - 1, self.y - 1], [self.x + 1, self.y - 1], 
					[self.x + 1, self.y + 1], [self.x - 1, self.y + 1]
					]
		for position in positions:
			if is_valid(position[0], position[1]):
				octopus[position[1]][position[0]].value += 1

def is_valid(x: int, y: int) -> bool:
		return (0 <= x < len(octopus[0])) and (0 <= y < len(octopus))

def octoSync() -> bool:
	return all([octopus[i][n].flash for i in range(len(octopus)) for n in range(len(octopus[0]))])

def step() -> bool:
	for n in range(len(octopus)):
		for i in range(len(octopus[0])):
			octopus[i][n].value += 1

	while any(True for i in range(len(octopus)) for n in range(len(octopus[i])) if octopus[i][n].value > 9):
		for n in range(len(octopus)):
			for i in range(len(octopus[0])):
				if octopus[i][n].value > 9 and not octopus[i][n].flash:
					octopus[i][n].Flash()
	
	if octoSync():
		return True
	
	for n in range(len(octopus)):
		for i in range(len(octopus[0])):
			octopus[i][n].flash = False

	return False
octopus:Octopus = []

with open('data.txt', 'r') as data_file:
	lines = [line.strip() for line in data_file]
	for i in range(len(lines)):
		octopus.append([])
		for n in range(len(lines[i])):
			octopus[i].append(Octopus(n, i, lines[i][n], False))

countStep = 0
while True:
	countStep += 1
	if step():
		print(countStep)
		break

	
class Color:
	'''
	Class that encapsulate color name, hex code, and type of plant it represents
	'''
	def __init__(self, num, plant):
		self.num = num
		self.plant = plant

	def __repr__(self):
		return self.plant + " " + str(self.num)

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.plant == other.plant
		else:
			return False
	
	def __hash__(self):
		return hash(self.plant)
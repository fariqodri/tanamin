class Color:
	'''
	Class that encapsulate color name, hex code, and type of plant it represents
	'''
	def __init__(self, num, plant):
		self.num = num
		self.plant = plant

	def __repr__(self):
		return self.plant

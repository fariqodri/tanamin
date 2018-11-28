from csp.utils import Color

class Province:
	'''
	Class that encapsulate province name, area, and color it is represented
	'''
	def __init__(self, name, area, color: Color=None):
		self.name = name
		self.area = area
		self.color = color
	
	def get_color(self):
		return self.color
	
	def set_color(self, color: Color):
		self.color = color
	
	def get_name(self):
		return self.name

	def __repr__(self):
		return self.name + " " + str(self.color)

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.name == other.name
		else:
			return False

	def __hash__(self):
		return hash(self.name)
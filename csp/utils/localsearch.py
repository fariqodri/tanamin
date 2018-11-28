from load_csv.models import Province as ProvinceModel
from csp.utils import Province
import random
import math

class LocalSearch:
	def __init__(self, csp):
		self.csp = csp
	
	def check_solution(self, current):
		# d = {}
		# for prov in current:
		# 	d[prov] = prov
		# for a,b in self.csp.constraints:
		# 	# print(a[0], a[1])
		# 	if d[a].color == d[b].color:
		# if self.calculate_conflicts(current) != 0:
		# 		return False
		# return True
		for a,b in self.csp.constraints:
			if current[a.name].color == current[b.name].color:
				return False
		return True

	def conflicted_variable(self, current):
		print("CONFLICTED VARS")
		d = {}
		vars = []
		for a,b in self.csp.graph.generate_edges():
			if current[a.name].color == current[b.name].color:
				if (a not in vars):
					vars.append(a)
				if (b not in vars):
					vars.append(b)
		return vars

	def conflicts(self, variable, value, current):
		province = current[variable.name]
		province.set_color(value)
		current[variable.name] = province
		return self.calculate_conflicts(current)

	def calculate_conflicts(self, current):
		count = 0
		for a,b in self.csp.constraints:
			if current[a.name].color == current[b.name].color:
				count += 1
		return count
	
	def assign(self):
		print("ASSIGN")
		AREA = 8087393
		area_divided = AREA // 4
		color_area = []
		result = {}
		for i in self.csp.domains:
			color_area.append([i, area_divided])
		for province in self.csp.variables:
			color_area.sort(key=lambda x: x[1], reverse=True)
			color, area = color_area[0]
			province.set_color(color)
			color_area[0][1] -= province.area
			result[province.name] = province
		return result

	'''CARI VALUE YANG BISA MEMINIMALISIR KONFLIK DAN MEMPERTAHANKAN KONSISTENSI LUAS'''
	def find_value(self, var, current):
		print("FIND VALUE")
		confs = self.calculate_conflicts(current)
		curr_confs = 100000000000
		current_copy = current
		prev_value = 0
		for value in self.csp.domains:
			curr_confs = self.conflicts(var, value, current)
			if (curr_confs < confs):
				return value

	def min_conflicts(self, max_steps=100):
		current = self.assign()
		for i in range(max_steps):
			print("iter:", i, ", conflicts: ", self.calculate_conflicts(current))
			if self.check_solution(current):
				return current
			conflicts = self.conflicted_variable(current)
			var = conflicts[random.randint(0, len(conflicts) - 1)]
			value = self.find_value(var, current)
			if value:
				current[var.name].set_color(value)
		return current
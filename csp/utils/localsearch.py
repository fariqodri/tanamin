from load_csv.models import Province as ProvinceModel
from csp.utils import Province
import random
import math

class LocalSearch:
	def __init__(self, csp):
		self.csp = csp
	
	def check_solution(self, current):
		d = {}
		for prov in current:
			d[prov] = prov
		for a,b in self.csp.constraints:
			# print(a[0], a[1])
			if d[a].color == d[b].color:
		# print("CHECK SOLUTION")
		# if self.calculate_conflicts(current) != 0:
				return False
		return True

	def conflicted_variable(self, current):
		print("CONFLICTED VARS")
		d = {}
		vars = []
		for prov in current:
			d[prov] = prov
		for a,b in self.csp.graph.generate_edges():
			if d[a].color == d[b].color:
				if (a not in vars):
					vars.append(a)
				if (b not in vars):
					vars.append(b)
		return vars

	def conflicts(self, variable, value, current):
		print("CONFLICTS")
		for i in range(len(current)):
			province = current[i]
			if province.get_name() == variable.get_name():
				current[i].set_color(value)
				return self.calculate_conflicts(current)

	def calculate_conflicts(self, current):
		# print("CALCULATE")
		count = 0
		provs = {}
		for prov in current:
			provs[prov] = prov
		for a,b in self.csp.constraints:
			if provs[a].get_color() == provs[b].get_color():
				count += 1
		print(count)
		return count
	
	def assign(self):
		print("ASSIGN")
		AREA = 8087393
		area_divided = AREA // 4
		color_area = []
		province_list = self.csp.variables
		for i in self.csp.domains:
			color_area.append([i, area_divided])
		for province in province_list:
			color_area.sort(key=lambda x: x[1], reverse=True)
			color, area = color_area[0]
			province.set_color(color)
			color_area[0][1] -= province.area
		self.csp.variables = province_list
		return province_list

	'''CARI VALUE YANG BISA MEMINIMALISIR KONFLIK DAN MEMPERTAHANKAN KONSISTENSI LUAS'''
	def find_value(self, var, current):
		print("FIND VALUE")
		confs = self.calculate_conflicts(current)
		curr_confs = 100000000000
		current_copy = current
		while(True):
			value = self.csp.domains[random.randint(0, len(self.csp.domains) - 1)]
			curr_confs = self.conflicts(var, value, current)
			if (curr_confs < confs):
				return value
			# nearests = sorted(current, key=lambda x: math.abs(x.area - var.area))[1:]
			# swapped = nearests[0]
			
			# for i in range(len(current_copy)):
			# 	if current_copy[i] == var:
			# 		for j in range
			# var.set_color(swapped.color)
			# if 

	def min_conflicts(self, max_steps=10000):
		current = list(self.assign())
		for i in range(max_steps):
			# print(i, self.calculate_conflicts(current))
			if self.check_solution(current):
				print("FOUND")
				return current
			conflicts = self.conflicted_variable(current)
			var = conflicts[random.randint(0, len(conflicts) - 1)]
			value = self.find_value(var, current)
			for i in range(len(current)):
				if (current[i] == var):
					current[i].set_color(value)
		return current
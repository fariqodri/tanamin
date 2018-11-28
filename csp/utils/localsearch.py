from load_csv.models import Province as ProvinceModel
from csp.utils import Province, Color
import random
import math
from collections import defaultdict

class LocalSearch:
	def __init__(self, csp, big_to_small=True):
		self.csp = csp
		self.big_to_small = big_to_small
	
	def check_solution(self, current):
		for a,b in self.csp.constraints:
			if current[a.name].color == current[b.name].color:
				return False
		return True

	def conflicted_variable(self, current):
		vars = []
		for a,b in self.csp.graph.generate_edges():
			if current[a.name].color == current[b.name].color:
				if (a not in vars):
					vars.append(current[a.name])
				if (b not in vars):
					vars.append(current[b.name])
		return vars

	def conflicts(self, variable, value, current):
		province = current[variable.name]
		province.set_color(value)
		current[variable.name] = province
		return self.calculate_conflicts(current)

	def color_heuristic(self, variable, value, current):
		current[variable.name].set_color(value)
		max_color = self.find_biggest_color(current)
		min_color = self.find_smallest_color(current)
		if self.get_area_of_color(max_color, current) - self.get_area_of_color(min_color, current) >= 200000:
			return False
		return True

	def calculate_conflicts(self, current):
		count = 0
		for a,b in self.csp.graph.generate_edges():
			if current[a.name].color == current[b.name].color:
				# print(current[a.name], current[b.name])
				count += 1
		return count
	
	def assign(self):
		# print("ASSIGN")
		AREA = 8087393
		area_divided = AREA // 4
		self.max_area = area_divided
		color_area = []
		result = {}
		for i in self.csp.domains:
			color_area.append([i, area_divided])
		self.csp.variables.sort(key=lambda x:x.area, reverse=self.big_to_small)
		self.color_area = dict(color_area.copy())
		assigned_provinces = set()
		while not len(assigned_provinces) == len(self.csp.variables):
			province = self.csp.variables[random.randint(0, len(self.csp.variables)-1)]
			if not assigned_provinces.__contains__(province):
				color_area.sort(key=lambda x: x[1], reverse=True)
				# idx = random.randint(0, len(color_area) - 1)
				color, area = color_area[0]
				province.set_color(color)
				color_area[0][1] -= province.area
				result[province.name] = province
				assigned_provinces.add(province)
		result = dict(sorted(result.items(), key=lambda x : x[1].area, reverse=True))
		# print(result)
		return result

	'''CARI VALUE YANG BISA MEMINIMALISIR KONFLIK DAN MEMPERTAHANKAN KONSISTENSI LUAS'''
	def find_value(self, var, current):
		confs = self.calculate_conflicts(current)
		for value in self.csp.domains:
			if self.conflicts(var, value, current) < confs and self.color_heuristic(var, value, current):
					return value
		smallest = self.find_smallest_color(current)
		print("sml", smallest)
		return smallest

	def find_smallest_color(self, current):
		r = self.get_color_data(current)
		# for c in self.csp.domains:
		# 	r[c] = self.get_area_of_color(c, current)
		r = dict(sorted(r.items(), key=lambda x:x[1]))
		return list(r.keys())[0]
	
	def find_biggest_color(self, current):
		r = self.get_color_data(current)
		# for c in self.csp.domains:
		# 	r[c] = self.get_area_of_color(c, current)
		r = dict(sorted(r.items(), key=lambda x:x[1], reverse=True))
		return list(r.keys())[0]

	def get_area_of_color(self, color, current):
		# count = 0
		# for i in current:
		# 	if current[i].color == color:
		# 		count += current[i].area
		# return count
		return self.get_color_data(current)[color]
	
	def get_color_data(self, current):
		keys = list(self.color_area.keys())
		res = dict()
		for k,v in current.items():
			if v.color in res:
				res[v.color] += v.area
			else:
				res[v.color] = v.area
		return res

	def min_conflicts(self, max_steps=10000):
		current = self.assign()
		prev_confs = self.calculate_conflicts(current)
		same_times = 0
		count = 0
		while count < 100000:
			for i in range(max_steps):
				confs = self.calculate_conflicts(current)
				if self.check_solution(current):
					return current
				conflicts = self.conflicted_variable(current)
				var = conflicts[random.randint(0, len(conflicts) - 1)]
				value = self.find_value(var, current)
				prev_confs = confs
				print(same_times)
				current[var.name].set_color(value)
				if prev_confs <= confs:
					same_times += 1
				if prev_confs <= confs and same_times >= 1000:
					break
			if prev_confs <= 3:
				break
			else:
				current = self.assign()
				prev_confs = self.calculate_conflicts(current)
			count += 1
		print(self.get_color_data(current))
		return current, self.conflicted_variable(current)
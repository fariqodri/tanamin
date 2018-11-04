class Color:
  def __init__(self, hex, plant):
    self.hex = hex
    self.plant = plant

class Province:
  def __init__(self, name, area, color=None):
    self.name = name
    self.area = area
    if isinstance(color, Color):
      self.color = color
    else:
      raise ValueError("color argument must be instance of Color object")
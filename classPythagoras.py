import math
class Pythagoras:
	
	def __init__(self,base, height):
		self.base=base
		self.height=height

	def area(self):
		return (0.5*self.base*self.height)
	
	def hypotenuse(self):
		return (math.sqrt((self.base**2)+(self.height**2)))

k=Pythagoras(7,4)
print(k.area())
print(k.hypotenuse())
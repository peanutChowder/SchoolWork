class Dog():
	def __init__(self, age=0, colour="brown", size="medium"):
		self.age = age
		self.colour = colour
		self.size= size

	def __str__(self):
		return f"I am a {self.colour} dog, of age {self.age}, of size {self.size}"

	def __repr__(self):
		return f"Id<{id(self)}> {self.colour} dog"

	def wag_tail(self):
		print(f"See my {self.colour} tail wagging slowly")

	def bark(self, barkVol="loudly"):
		print(f"I am barking {barkVol} said the {self.colour} dog!")

class Cat(Dog):
	def meow(self):
		print("meow")

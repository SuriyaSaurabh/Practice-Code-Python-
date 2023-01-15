#METHOD OVERLOADING
class test:
	def add(x,y):
		print(x+y)

	def add(x,y,z):
		print(x+y+z)

test.add(10,20)#TypeError: test.add() missing 1 required positional argument: 'z'
test.add(10,20,30)

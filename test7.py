class test:
	x=100
	def __init__(self,z,y):
		self.z=z
		self.y=y
t=test(20,30)
print(t.z)
print(t.y)
print(test.x)
t.z=100
t.y=200
print(t.z)
print(t.y)
print(test.x)
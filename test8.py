class test:
	x=22
	def __init__(self,y,z):
		self.y=y
		self.z=z
t=test(20,30)
print(t.z)
print(t.x)
print(t.y)
print(test.x)
test.x=1000
test.y=2000
t.x=100
t.y=200
t.z=30
print(t.z)
print(t.x)
print(t.y)
print(test.y)
print(test.x)
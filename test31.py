z=1000
class test:
	x=10
	def __init__(self,y):
		self.y=y
	def m1(self):
		z=100
		print(test.x)
		print(self.y)
		print(z)
	def m2(self):
		print(test.x)
		print(self.y)
		print(z)

t=test(20)
t.m1()
t.m2()

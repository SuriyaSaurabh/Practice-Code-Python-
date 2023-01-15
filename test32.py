x=1000
class test:
	x=10
	def __init__(self,y):
		self.x=y

	def m1(self):
		global x
		x=100
		print(test.x)
		print(self.x)
		print(x)

	def m2(self):
		print(test.x)
		print(self.x)
		print(x)

t=test(20)
t.m1()
t.m2()
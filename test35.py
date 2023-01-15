class p:
	x=100
	def __init__(self,y):
		self.p=10
	def m1(self):
		self.q=20
class c(p):
	y=200

c=c(10)
print(c.x,c.y,c.p,)
c.m1()
print(c.x,c.y,c.p,c.q)

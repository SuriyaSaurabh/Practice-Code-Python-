class p:
	x=100
	def __init__(self,y):
		self.p=10
	def m1(self):
		self.q=20
class c(p):
	def __init__(self):
		self.r=40
	
	y=200

c=c()
print(c.x,c.y,c.r,)
c.m1()
print(c.x,c.y,c.r,c.q)

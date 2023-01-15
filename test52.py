class parent:
	x=100
	def __init__(self,a,x):
		self.a=a
		parent.x=x

class child(parent):
	y=200
	def __init__(self,a,x,b):
		super().__init__(a,x)
		#super().__init__(a,x)
		self.b=b

c=child(100,2000,300)
print(c.x,c.y,c.b,c.a)
print(c.y,c.x,c.b)
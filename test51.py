#IS-A VS HAS-A REALTION 
class parent:
	x=100
	def __init__(self):
		self.a=10

class child(parent):
	def __init__(self):
		self.b=20
	y=200
c=child()
#print(c.x,c.y,c.a,c.b)
print(c.x,c.y,c.b)
#IS-A VS HAS-A REALTION 
class parent:
	x=100
	def __init__(self):
		self.a=10

class child(parent):
	y=200
c=child()
print(c.x,c.y,c.a)
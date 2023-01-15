class test:
	x=100
	def __init__(self):
		self.x=10

t=test()
print(t.x)
del t.x 
print(t.x)


class test:
	x=10
	def __init__(self,y):
	  self.y=y
t=test(20)
print(t.x)
print(t.y)
print(test.x)
t.x=100
t.y=200
print(t.x)
print(t.y)
print(test.x)
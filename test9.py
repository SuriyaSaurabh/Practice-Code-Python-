class test:
	x=231
	def __init__(self,y):
	    self.y=y

t=test(20)
t1=test(30)
print(t.x,t.y)
print(t1.x,t1.y)
test.x=100
t.y=200
print(t.x,t.y)
print(t1.x,t1.y)
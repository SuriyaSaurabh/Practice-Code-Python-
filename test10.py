class test:
	x=10
	def __init__(self,y):
  	    self.y=y
  	    test.z=50
    def m1(self):
  	    test.x=400
  	    self.y=500
t=test(20)
t1=test(30)
print(t.x,t.y,t.z)
print(t1.x,t1.y,t1.z)
t.m1()
test.x=100
t1.x=300
t.y=200
print(t.x,t.y,t.z)
print(t1.x,t1.y,t1.z)
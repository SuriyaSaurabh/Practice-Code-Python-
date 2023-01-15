#CONSTRUCTOR OVERLOADING
class test:
	def __init__(self,a,b):
		print(x+y+z)

	def __init__(self,a,b,c):
		print(a+b+c)

t=test(10,20)#TypeError: test.__init__() missing 1 required positional argument: 'c'

t=test(10,20,30)

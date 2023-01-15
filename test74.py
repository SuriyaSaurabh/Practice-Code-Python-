#CONSTRUCTOR OVERLOADING
#by using variable length argument
class test:
	def __init__(self,*a):
		print(a)


t=test(10,20)
t=test(10,20,30)

#SUPER#
class A():
	def m1(self):
		print("A")

class B:
	def m1(self,b):
		b.m1()
		print('B')



a=A()
b=B()
b.m1(a)
b.m1(A())

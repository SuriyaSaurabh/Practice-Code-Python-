#SUPER#
class A():
	def m1(self):
		print("A")

class B(A):
	def m1(self,a):
		a.m1()
		print('B')



a=A()
b=B()
b.m1(a)

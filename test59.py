#SUPER#
class A():
	def m1(self):
		print("A")

class B(A):
	def m2(self):
		print('B')
		super().m1()

b=B()
b.m1()

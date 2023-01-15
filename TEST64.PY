#SUPER#
class A():
	def m1(self):
		print("A")

class B(A):
	def m1(self):
		print('B')

class C(B):
	def m1(self):
		print('C')
		super().m1()

c=C()
c.m1()

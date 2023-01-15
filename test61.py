#SUPER#
class A():
	def m2(self):
		print("A")

class B(A):
	def m1(self):
		print('B')
		self.m2()
		#super hta toh ese hoga program 

b=B()
b.m1()
b.m2()
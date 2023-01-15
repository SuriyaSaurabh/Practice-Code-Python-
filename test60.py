#SUPER#
class A():
	def m1(self):
		print("A")

class B(A):
	def m2(self):
		print('B')
		#super hta toh ese hoga program 

b=B()
b.m1()
b.m2()
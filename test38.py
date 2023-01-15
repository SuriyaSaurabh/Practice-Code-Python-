class A:
	def m1(self):
		print("A-m1")

class B(A):
	def m2(self):
		print("B-m2")

class C(B):
	def m3(self):
		print("C-m3")

class D(C):
	def m4(self):
		print("D-m4")

d=D()
d.m1()
d.m2()
d.m3()
d.m4()
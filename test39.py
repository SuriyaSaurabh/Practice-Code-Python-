class A:
	def m1(self):
		print("A-m1")

class B():
	def m2(self):
		print("B-m2")

class C(A,B):
	def m3(self):
		print("C-m3")

c=C()
c.m1()
c.m2()
c.m3()


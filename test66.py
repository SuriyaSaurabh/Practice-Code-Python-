#SUPER#
class A():
	def m1(self):
		print("A")

class B(A):
	def m1(self):
		super().m1()
		#super(B,self).m1()
		#super(A,self).m1() #ERROR==AttributeError: 'super' object has no attribute 'm1'

		print('B')

class C(B):
	def m1(self):
		print('C')
		super().m1() 
		super(B,self).m1()
		#super(c,self).m1()
		#super(A,self).m1()# error=AttributeError: 'super' object has no attribute 'm1'


c=C()
c.m1()


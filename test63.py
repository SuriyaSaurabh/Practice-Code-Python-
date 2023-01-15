#SUPER#
class A():
	def m1(self):
		print("A")

class B(A):
	def m1(self):
		print('B')
		A.m1(self)
		super().m1()
		#super().m1() ye bhi use kr skte h line 9 pe 
		#or line 9 pe abhi , static method bna class ke name pe call hua 


b=B()
b.m1()

#SUPER#
class A():
	def m2(self):
		print("A")

class B(A):
	def m1(self):
		print('B')
		A.m2(self)
		#super().m2()
		#super().m1() ye bhi use kr skte h line 9 pe 
		#or line 9 pe abhi , static method bna class ke name pe call hua 


b=B()
b.m1()
b.m2()
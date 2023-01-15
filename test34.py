class p:
	x=00
	def __init__(self):
		print('constructor')

	def m1(self):
		print('instance methord')

	@classmethod
	def m2(cls):
		print('class methord')

	@staticmethod
	def m3(self):
		print('static method')

class c(p):
	pass 
c=c()
c.m1()
c.m2()
c.m3(1)

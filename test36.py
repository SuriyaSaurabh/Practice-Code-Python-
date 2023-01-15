class p:
	pass 

class c(p):
	def m1(self):
		print('instance method')

p=p()
p.m1()
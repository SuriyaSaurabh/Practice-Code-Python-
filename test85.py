#DUCK typing philosophy of python
class duck:
	def talk(self):
		print("quack--quack")

class cat:
	def talk(self):
		print("meow--meow")

class dog:
	def talk(self):
		print("bow--bow")

def fun(obj):
	obj.talk()

d=duck()
c=cat()
d1=dog()
fun(c)
fun(d1)
fun(d)
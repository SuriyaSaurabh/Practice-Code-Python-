#DUCK typing philosophy of python
class duck:
	def talk(self):
		print("quack--quack")

class cat:
	def sound(self):
		print("meow--meow")

class dog:
	def talk(self):
		print("bow--bow")

def fun(obj):
	if hasattr(obj,"talk"):
		obj.talk()
	else:
	    obj.sound()



d=duck()
c=cat()
d1=dog()
fun(c)
fun(d1)
fun(d)
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
	elif hasattr(obj,"bark"):
	    obj.sound()
	else:
		obj.sound()

d=duck()
c=cat()
d1=dog()
fun(d)
fun(c)
fun(d1)
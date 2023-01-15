#METHOD OVER-RIDING
class parent:
	def property(self):
		print("glod+cash+power")

	def marry(self):
		print("abc")

class child(parent):
	def marry(self):
		print("pqr")

c=child()
c.property()
c.marry()


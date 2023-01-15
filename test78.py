#CONSTRUCTOR OVER-LOADING
class parent:
	def __init__(self):
		print("PARENT CONSTRUCTOR")

class child(parent):
	def __init__(self):
		print("CHILD CONSTRUCTOR")

c=child()




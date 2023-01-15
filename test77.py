#CONSTRUCTOR OVER-RIDING
class parent:
	def __init__(self):
		print("PARENT CONSTRUCTOR")

class child(parent):
	pass 
	#def __init__(self):
		#print("CHILD CONSTRUCTOR")

c=child()




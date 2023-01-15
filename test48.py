class car:
	def __init__(self,model,color):
		self.model=model
		self.color=color

	def getinfo(self):
		print(self.model)
		print(self.color)

class employee:
	def __init__(self,eid,esal,car):
		self.eid=eid
		self.esal=esal
		self.car=car

	def display(self):
		print(self.eid)
		print(self.esal)
		self.car.getinfo()

c=car("Honda","black")
e=employee(1,1000,c)
e.display()
e.car.getinfo()
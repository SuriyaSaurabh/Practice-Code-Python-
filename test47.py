class engine:
	def __init__(self):
	   self.a=10
	   def start(self):
	   		print("ENGINE_START")

class car:
	def __init__(self,model,en):
		self.model=model
		self.en=en

	def use_engine(self):
		print(self.model)
		self.en.start()
		#self.en.a()
		print(self.en.a)

e=engine()
c=car("Honda",e)
c.use_engine()


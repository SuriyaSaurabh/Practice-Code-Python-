#HAS-A RELATION
class engine:
	@staticmethod
	def start():
		print("ENGINE_START")

class car:
	def use_engine(self):
		engine.start()

c=car()
c.use_engine()
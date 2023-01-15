#HAS-A relation
class engine:
	def start(self):
		print('ENGINE-START')
 
class car:
#class start:
	def use_engine(self):
		e=engine()
		e.start()


#c=start()
c=car()
c.use_engine()

#refernce variable function 
#__str__
class book:
	def __init__(self,pages):
		self.pages=pages
	def __str__(self):
		return str(self.pages)

b1=book(300)
print(b1)
print(b1.__str__)
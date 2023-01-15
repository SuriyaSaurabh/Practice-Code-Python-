#OPERATOR OVER LOADING
#MAGIC METHOD
class book:
	def __init__(self,pages):
		self.pages=pages

	def __add__(self,other):      #magic method
		return self.pages+other.pages 

b1=book(300)
b2=book(150)
b3=book(200)
print(b1+b2)
print(b1+b3)
print(b2+b3)
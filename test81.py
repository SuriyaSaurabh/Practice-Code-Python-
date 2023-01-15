#opertor overloading
class employee:
	def __init__(self,name,d_salary):
		self.name=name
		self.d_salary=d_salary
	def __mul__(self,other):  #magic method
		return self.d_salary*other.days

class timesheet:
	def __init__(self,name,days):
		self.name=name
		self.days=days

	def __mul__(self,other): #magic method
		return other.d_salary*self.days
		
e=employee("abc",200)
t=timesheet("abc",22)
print(e*t)
print(t*e)

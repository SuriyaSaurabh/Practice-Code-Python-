class student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
	def m1(self):
			self.age=27
			self.contact=1234
	def m2(self,collage,id):
		self.collage=collage
		self.id=id

s1=student(1,"abc")
s2=student(2,"pqr")
print(s1.__dict__)
print(s2.__dict__)
s1.m1()
s2.m2("ssss",16461)
print(s1.__dict__)
print(s2.__dict__)

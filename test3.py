class studen:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
	def m1(self,age,contact):
		self.age=age
		self.contact=contact

s1=studen(100,"SAURABH")
s2=studen(101,"SHARMA")
print(s1.__dict__)
print(s2.__dict__)
s1.m1(12,456745688)
s1.contact=7896366363
s2.contact=989898989
print(s1.__dict__)
print(s2.__dict__)
		
class student:
	def __init__(self,rno,nm):
		self.rollno=rno
		self.name=nm

s=student(1,"abc")
s1=student(2,"xyz")
s2=student(3,"csd")
print(s2.__dict__)
print(s2.__dict__)
s1.age=27
print(s1.__dict__)
print(s1.__dict__)

class student:
	cname="cpt"
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
		student.cadd="jaipur"


print(student.__dict__)
s=student(1,"csd")
print(s.__dict__)
print(s.__dict__)
print(student.__dict__)

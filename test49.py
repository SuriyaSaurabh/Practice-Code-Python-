class student:
	cname="cpt"
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name


c=student(222,'fmjndi')
print(student.cname)
c=student(123,"abc")
print(c.rollno)

print(c.name)
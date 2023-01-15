class student:
	cname="codeplanet"
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
	def display(self):
		print(self.rollno,self.name)

		

	@classmethod
	def cdisplay(cls):
		print(student.cname)
		print(cls.cname)


s=student(1,"csd")
s1=student(97,'saurbh')
s.display()
s1.display()
student.cdisplay()

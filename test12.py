class student:
	def __init__(self,rollno,name,marks):
		self.rollno=rollno
		self.name=name
		self.marks=marks
	def display(self):
		print(self.rollno,self.name)
	def grade (self):
	 if self.marks>60:
	  print("first grade")
	 elif self.marks>45:
	  print("second grade")
	 elif self.marks>35:
	 	print("third grade")
	 else:
	 	print("fall")
s1=student(1,"csd",100)
s2=student(2,"cpt",10)
s1.display()
s2.display()
s1.grade()
s2.grade()
class student:
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
		print(self.rollno,self.name)
	def cert(self,cert):
		self.cert=cert
		print(self.cert)


s=student(1,"abc")
s1=student(2,"csd")
s2=student(3,"pqr")
s3=student(14,"xyz")
s1.cert("AVM")
s3=student(14,"xyz")
s2.cert("CPT")
s.cert("csd1")

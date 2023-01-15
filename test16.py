class student:
	count=0
	def __init__(self):
		student.count=student.count+1

	@classmethod
	def noofobjects(cls):
			print(cls.count)

s=student()
s1=student()
s2=student()
student.noofobjects()
s3=student()
s4=student()
student.noofobjects()

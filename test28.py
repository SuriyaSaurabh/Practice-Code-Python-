import time
class student:
	def __init__(self):
		print("constructor")

	def __del__(self):
		print("destructor")

s=student()
time.sleep(3)
s1=student()
s2=student()
s3=student()
time.sleep(2)
print("END")





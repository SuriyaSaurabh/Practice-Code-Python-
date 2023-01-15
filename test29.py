import time
class student:
	def __init__(self):
		print("constructor")

	def __del__(self):
		print("destructor")

s=student()
s1=student()
print("hello")
del s1
time.sleep(3)
print("hello1")
print("END")
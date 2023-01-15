import time 
class student:
	def __init__(self):
		print("constructor")


	def __del__(self):
		print("destructor")

s=student()
s1=student()
s=s1
time.sleep(3)
print("hello")
del s
time.sleep(2)
print('hello1')
del s1 
time.sleep(1)
print("END")


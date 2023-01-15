import time
class student:
	def __init__(self):
		print("constructor")
	def __del__(self):
		print("destructor")


s=student()
s1=s
del s
time.sleep(3)
print("HELLO")
del s1
time.sleep(3)
print("HELLO 1")
print('END')

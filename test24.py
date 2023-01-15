import time
class student:
	def __init__(self):
		print("constructor")

	def __del__(self):
		print("destructor")

s=student()
s1=student()
s2=s
del s
del s1
time.sleep(3)
print("HELLO")
del s2
time.sleep(3)
print("HELLO 1")
time.sleep(2)
print("END")
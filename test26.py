import time
class student:
	def __init__(self):
		print("constructor")

	def __del__(self):
		print("destructor")

s=student()
del s
time.sleep(3)
print("END")

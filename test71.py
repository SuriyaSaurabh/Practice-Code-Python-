#METHOD OVERLOADING
#by using variable length argument
class test:
	def add(*n):
		result=0
		for num in n:
			#result=0
			result=result+num
		print(result)

test.add(10,20)
test.add(10,20,30)
test.add(10,20,30,40)
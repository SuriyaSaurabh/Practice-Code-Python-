import sys
class test:
	pass 

t=test()
t1=test()
t2=t
t3=t
t4=t
t5=t1
print(sys.getrefcount(t))
print(sys.getrefcount(t1))
print(sys.getrefcount(t5))


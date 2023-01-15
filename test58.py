def csd():
	print('suriya')

x=csd()
y=csd
y()
#x() # none type error apper 
print(id(csd))
print(id(y))
print(id(x))
print(csd is y)
print(csd is x)
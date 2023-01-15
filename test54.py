#function aliasing
def csd():
	print("this is function")
csd()#function calling
y=csd()
x=csd #function aliasing here 
x() # calling function
y() #NoneType' object is not callable error apper 
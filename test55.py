#function aliasing
def csd():
	print("CSD")

def csd1():
	print("CSD1")


csd()#function calling
x=csd()
x=csd1()
y=csd1()
z=csd
z1=csd1 #function aliasing here 
csd=csd1
z()
z1()
csd()
csd1()
x() # calling function ,#NoneType' object is not callable error apper 
Y() #NoneType' object is not callable error apper 
#File handling
f= open ("abc.txt", 'w')
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
#print(f.closed())#TypeError: 'bool' object is not callable
f.cl()         #TypeError: 'bool' object is not callable
print(f.closed())   #TypeError: 'bool' object is not callable
print()
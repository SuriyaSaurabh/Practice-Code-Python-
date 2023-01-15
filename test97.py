#nesting of opertor on non-boolen 
x= 10 and 20 and 30
y= 10 or 20 and 30
p= 10 and 20 or 30
q= 10 or 20 or 30
print(x,y,p,q)
print()
x=() and 20
y=0 and ()
p=[] and 30
q=[] and 0 
print(x,y,p,q)
print()

x=() or 20
y=0 or  ()
p=[] or 30
q=[] or  0
print(x,y,p,q)
print()

x=() and 20 and ()
y=0 and () and 60
p=[] and 30 and ()
q=[] and () and []
r=() and () and []
s=[] and () and []
print(x,y,p,q,r,s)
print()

x=() or 20 or ()
y=0 or () or 60
p=[] or 30 or ()
q=[] or () or []
r=() or () or []
s=[] or () or []
print(x,y,p,q,r,s)
print()

x=() and 20 or ()
y=0 or () and 60
p=[] and 30 or ()
q=[] and () or []
r=() or () and []
s=[] or 0 and []
print(x,y,p,q,r,s)
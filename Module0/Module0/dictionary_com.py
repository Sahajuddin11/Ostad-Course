li = [(1,'one'),(2,'two'),(3,'three')]
print(li)
print(type(li))
dt = {a:b for a,b in li}
print(dt)
print(type(dt))
dt = {a:b for b,a in li}
print(dt)
print(type(dt))

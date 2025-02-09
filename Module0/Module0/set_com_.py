a = "sahajuddinahmed"
s = {c for c in a}
print(s)
print(type(s))

color_choice = [('Messi','Blue'),('Ronaldo','Red'),('Naymer','Yellow'),('Dimariya','Blue')]
print(color_choice)
print(type(color_choice))

color_dt = {name:color for name,color in color_choice}
print(color_dt)
print(type(color_dt))

s = {c for c in color_dt.values()}
print(s)
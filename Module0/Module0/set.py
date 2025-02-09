s =set()
print(type(s))
s1 = {1,2,3,4}
s2 = {2,4,5,6}

s3= s1 | s2 # union or all value for s1 and s2
print(s3)

s4= s1 & s2 # intersection or common
print(s4)

s5 = s1 - s2 #s1 have but s2 don't have
print(s5)

s6 = s1 ^ s2 #X-OR don't match to others
print(s6)

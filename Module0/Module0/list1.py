li = [1,2,3,4]
li2 = [5,6,7,8]

li = li + li2
#print(li)

li = [1,2,3,4]
li2 = [5,6,7,8]

li.extend(li2)
#print(li)

li = [1,3,4,5]
li.insert(1,8)
#print(li)

li = [1,3,4,55,5]
#print(li.index(5))

li = [1,3,4,55,5,4,6,7,1]
li.remove(3)
#print(li)

li = [1,3,4,55,5,4,6,7,1]
li.pop()#li.pop(index)
#print(li)

li = [1,3,4,55,5,4,6,7,1]
li.sort()
#print(li)
#li = [1,3,4,55,5,4,6,7,1]
li.reverse()
#print(li)
#print(dir(list))

#print(dir(tuple))




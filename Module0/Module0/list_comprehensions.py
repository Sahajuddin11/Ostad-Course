li = ['apple','banana','orange','mango','guava']
fruits =[frut.capitalize() for frut in li]
print(fruits)

li_len = [len(x) for x in li]
print(li_len)

cube_list = [x*x*x for x in range(1,11)]
print(cube_list)

cube_list_if = [x*x*x for x in range(1,11) if x%2 ==1]
print(cube_list_if)

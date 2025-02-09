li = [1,2,3,4,10,11,234,2,5]
n = 5
flag = False
for num in li:
    if n == num:
        print("Yes")
        flag = True
        break
    
if flag == False:      
    print("No")
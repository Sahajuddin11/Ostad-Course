li =[10,2,100,3,500,5]
print("List : ",li)

max_number = max(li)
print("The max Number ",max_number)

mex = li[0]
for num in li:
    if mex < num:
      mex=num
print("The max Number ",mex)
    
min_number = min(li)
print("The min Number ",min_number)
min = li[0]
for num in li:
    if min > num:
      min=num
print("The min Number ",min)

sum_number = sum(li)
print("The sum Number ",sum_number)
Sum = 0
for num in li:
    Sum=Sum+num
print("The sum Number ",Sum)


mul = 1
for num in li:
    mul = mul * num
print("The mul Number ",mul)


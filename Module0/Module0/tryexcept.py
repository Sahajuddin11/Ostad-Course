while True:
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    
    if n1 == 0 and n2 == 0:
        break
    try:
     print("The result ", n1/n2)
    except ZeroDivisionError:
        print("Zero can't divided ")
    else:
        print("Good Work $")
 
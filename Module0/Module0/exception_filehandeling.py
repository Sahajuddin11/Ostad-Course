try:
 fp = open("mynewfile.txt",'w')
 list1 = ['apple ',' banana ',' orange ',' mango ',' guava ']
 fp.writelines(list1)
 fp.write("this is a test file\n")
 fp.close()
except FileNotFoundError:
    print("Your file is no found")
print("Complete your code done")
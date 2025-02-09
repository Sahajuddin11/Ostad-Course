fp = open("myfile.txt",'a')
list1 = ['apple ',' banana ',' orange ',' mango ',' guava ']
fp.writelines(list1)
fp.write("this is a test file\n")
#content = fp.read()
fp.close()
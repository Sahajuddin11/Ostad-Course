import math

class fraction:
    def __init__(self,n,d):#__ mean dendar methon or magic method / constractor
        self.numerator = n
        self.denominator = d
        
    def add(self,f):
       g = math.lcm(self.denominator, f.denominator) 
       num = (g / self.denominator)* self.numerator +(g / f.denominator)* f.numerator
       self.numerator = int(num)
      
       self.denominator = g
       
    def __add__(self,f):
       g = math.lcm(self.denominator, f.denominator) 
       num = ((g / self.denominator)* self.numerator) + (g / f.denominator)* f.numerator
      
       return fraction(num,g)
   
    def __str__(self):
        return "{}/ {}".format(self.numerator, self.denominator)
    
    def __eq__(self, f):
        g = math.gcd(self.numerator, self.denominator)
        num1 = int(self.numerator/g)
        denom1 = int(self.denominator/g)
        
        g = math.gcd(f.numerator, f.denominator)
        num2= int(f.numerator/g)
        denom2 = int(f.denominator/g)
        
        return num1 == num2 and denom1== denom2



f1 = fraction(5,10)#1/2
f2 = fraction(10,20)#1/5


#f1.add(f2)
result = f1 + f2
print(f1,f2)

print(result)
print(result.numerator, result.denominator)

print(f1 == f2)
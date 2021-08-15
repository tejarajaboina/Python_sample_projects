def myfunc1(a):
   print("\t inside myfunc1()")
   print("\t value of 'a'as",a)
   a=a+2
   print("\t value of 'a' now changes to",a)
   print("\t returning from myfunc1()")

#__main__

num=3
print("calling myfunc1() by passing 'num' with value",num)
myfunc1(num)
num=num+1
print("back frommyfunc1().value of 'num' is",num)      
      

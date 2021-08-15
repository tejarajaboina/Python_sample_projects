######
# if w is replased with r+ 
######


f=open("test2.txt","r+")

stu=int(input("enter number of students: "))

for i in range(stu):
    name=input("enter name of the students: ")

    roll=int(input("enter the roll no of "+name+" :"))

    marks=int(input("enter the marks of "+name+" :"))

    a=name+","+str(roll)+","+str(marks)+'\n'
    f.write(a)

f.close()

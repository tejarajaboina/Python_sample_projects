#+++++++++++++++++++++++++++++++++++++++++++
# This code will create file test1.txt 
# promts basic info of student and append data to test1.txt file with , seperation

# used 
#if
#elif
#for
#type casinting (int to str , str to int)
# open file
# write to file
# close file

#++++++++++++++++++++++++++++++++++++++++++++

a=open("test1.txt","a")
num_stu=int(input("How many students data you want to enter:"))
for i in range(num_stu):
   
    stu_name=input("enter the the name of the student: ")
    a.write(stu_name+',')
    stu_class=input("enter class of the " +stu_name+" : ")
    
    passed_clas=int(stu_class)-1
    passed_class=str(passed_clas)
    a.write(stu_class+',')
    perc=int(input("percentage scored in class" +passed_class+ ": "))
    percentage=str(perc)
    a.write(percentage+',')
    if 30<perc<=50:
      print(stu_name+" is in section D")
      a.write("D")
    elif 50<perc<=60:
        print(stu_name+" is in section c")
        a.write("C")
    elif 60<perc<=70:
        print(stu_name+" is in section B")
        a.write("B")
    elif 70<perc<100:
        print(stu_name+" is in section A")
        a.write("A")
    else:
        print("not promoted")
        a.write("FAIL")




    print("we have saved information !!")
    #a.write(stu_num+'\n')
    a.write('\n')
a.close()    

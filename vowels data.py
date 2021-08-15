f=open("test2.txt","r")
vcount=0
    #count=
for i in range(100):
    
    if(f.read(1)) in ['a','e','i','o','u']:
        
        vcount=vcount+1

print(vcount)

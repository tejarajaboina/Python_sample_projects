alist=(1,4,68,9,0,210,444,555,00,2)
print("original list:",alist)
n=len(alist)
for i in range(n):

    for j in range(0,n-i-1):
        if alist(j)>alist(j+1):
            alist(j),alist(j+1)=alist(j+1),alist(j)
        
print("list after bubblesort:",alist)        

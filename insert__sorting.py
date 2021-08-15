alist=[11,222,3,7,8,90]
print("original list:",alist)
for i in range(1,len(alist)):
     key=alist[i]
     j=i-1
     while j>=0 and key<alist[j]:
        alist[j+1]=alist[j]
        j=j-1
     else:
          alist[j+1]=key

print("list after sorting:",alist)          

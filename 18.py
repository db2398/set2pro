snit1,smit1=map(int,input().split())
tem1=[]
x=0
for m in range(snit1):
    tem1.append(list(map(int,input().split())))   
for m in range(snit1):
    for j in range(smit1-1):
        for k in range(j+1,smit1+1):
            if tem1[m][j:k]==[1]*len(tem1[m][j:k]):
                 if all(tem1[p+m][j:k]==[1]*len(tem1[p+m][j:k]) for p in range(len(tem1[m][j:k])-1)):
                     if len(tem1[m][j:k])>x:
                        x=len(tem1[m][j:k])
if len(tem1)==1 and len(tem1[0])==1 and tem1[0][0]==1:
    print(1)
for m in range(x):
    print(*[1]*x) 

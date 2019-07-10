sure=int(input())
cine=list(map(int,input().split()))
ss=[1]*sure
for i in range(sure):
    if i==0:
        if cine[i]>cine[i+1]:
            ss[i]=ss[i]+ss[i+1]
    elif i>0:
        if cine[i]>cine[i-1]:
            ss[i]=ss[i]+ss[i-1]
print(sum(ss))

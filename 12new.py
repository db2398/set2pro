aa2,bb2=map(int,input().split())
ls=list(map(int,input().split()))
l2=[]
for i in range(0,bb2):
     uu2,vv2=map(int,input().split())
     l2.append([uu2,vv2])
for i in range(bb2):
     lower=l2[i][0]
     upper=l2[i][1]
     ss2=sum(ls[lower-1:upper])
     print(ss2)

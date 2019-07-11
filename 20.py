jaat1=input().split()
total1=int(jaat1[0])
penny=int(jaat1[1])
l=input().split()
l=[int(i) for i in l]
l=sorted(l,reverse=True)
tem=0
count=0
for i in range(0,len(l)):
  while True:
    if(tem==penny):
      break
    elif(tem>penny):
      count-=1
      tem-=l[i]
      break
    elif(tem<penny):
      tem+=l[i]
      count+=1
print(count)

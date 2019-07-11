count16=int(input())
array=[]
vvv2=[]
for i in range(count16):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        vvv2.append(num)
vvv2.sort()
for i in vvv2:
    print(i,end=' ')

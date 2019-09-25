n=input()
a=[]
count=0
count1=0
for i in range(len(n)):
    a.append(int(n[i]))

for j in range(len(a)):
    if(a[j]==1):
        count=count+1
    elif(a[j]==0):
        count1=count1+1

if(count1==1):
    print("YES",end="")
elif(count==1):
    print("YES",end="")
else:
    print("NO",end="")
n=input()
b=n.split()
a=[]
count=0
for i in b:
    a.append(int(i))
    count=count+1

a.sort()
print(a[count-2],a[1],end="")
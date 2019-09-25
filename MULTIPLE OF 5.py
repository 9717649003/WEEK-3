n=input()
b=n.split()
a=[]
for i in b:
    if(int(i)%5==0):
        continue
    else:
        a.append(int(i))
z=len(a)
for j in range(z-1):
    print(a[j],end=" ")
print(a[z-1],end="")
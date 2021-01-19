n=4
k=3
x=2
if x!=1:
    a=[0]
    b=[1]
else:
    a=[1]
    b=[0]
for i in range(1,n):
    a.append(b[-1]%(10**9+7))
    b.append((a[-2]*(k-1)+b[-1]*(k-2))%(10**9+7))
print(a)
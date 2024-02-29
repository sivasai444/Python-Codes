n=input("Enter the number:")
m=str(n)
a=m[:len(m)//2]
b=m[len(m)//2:]
c=int(a)+int(b)
d=c**2
print(n,a,b,c,d)
if d==n:
    print("Yes")
else:
    print("No")

n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
print(sum)
if(sum==n):
    print("Yes")
else:
    print("No")

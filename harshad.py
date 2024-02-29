n=int(input("Enter the number:"))
sum=0
temp=n
while n!=0:
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)
if temp%sum==0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")

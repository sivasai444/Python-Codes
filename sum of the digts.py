n=int(input("enter the n:"))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("the sum of the digits is:",sum)

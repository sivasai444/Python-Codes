n=int(input("entre the value of n:"))
if n>1:
  for i in range(2,int(n/2)+1):
    if n%i==0:
        print(n,"not a prime num")
        break
    else:
        print(n,"is a prime num")
  

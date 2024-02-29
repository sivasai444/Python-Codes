def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divided (x,y):
    if y !=0:
        return x/y
    else:
        return "cannot divide by zero"

n=float(input("enter the value of n:"))
operator=input("enter the operator (+,-,*,/):")
m=float(input("enter the value of m:"))
if operator=="+":
    result=add(n,m)
elif operator=="-":
    result=subtract(n,m)
elif operator=="*":
    result=multiply(n,m)
elif operator=="/":
    result=divided(n,m)
else:
    result="invalid operator"

print(f"result:{result}")

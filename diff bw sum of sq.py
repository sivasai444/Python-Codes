def sum_of_square(n):
    return sum(i**2 for i in range(1,n+1))
def square_of_sum(n):
    return sum(range(1,n+1))**2
n=int(input("entre the numbers:"))
difference=sum_of_square(n)-square_of_sum(n)
print(f"the difference is:{difference}")

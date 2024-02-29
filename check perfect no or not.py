def is_perfect_number(num):
    sum_of_factors = 1  
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_of_factors += i
            if i != num // i:  
                sum_of_factors += num // i
    return sum_of_factors == num

def factors_of_number(num, m):
    factors = []
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
            count += 1
            if count == m:
                break
    return factors

def generate_perfect_numbers(n, m):
    perfect_numbers = []
    num = 2  
    while len(perfect_numbers) < n:
        if is_perfect_number(num):
            perfect_numbers.append(num)
        num += 1

    for perfect_num in perfect_numbers:
        print(f"Perfect Number: {perfect_num}, Factors: {factors_of_number(perfect_num, m)}")

N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))

generate_perfect_numbers(N, M)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num_of_primes = 0
num_of_composites = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input.lower() == 'done':
        break

    try:
        number = int(user_input)
        if is_prime(number):
            num_of_primes += 1
        else:
            num_of_composites += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Number of prime numbers:", num_of_primes)
print("Number of composite numbers:", num_of_composites)

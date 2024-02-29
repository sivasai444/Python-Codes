def sequential_digits(low,high):
    result=[]

    for num in range(1,10):
        current=num
        next_digit=num

        while current<=high and next_digit < 10:
            if current >= low:
                result.append(current)

            next_digit +=1
            current = current * 10 + next_digit

        return sorted(result)
print( sequential_digits(100,300))
print( sequential_digits(1000,13000))

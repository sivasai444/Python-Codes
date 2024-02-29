def min_jumps_to_reach_end(arr):
    n = len(arr)
    if n <= 1:
        return 0

    jumps = 1  
    max_reach = arr[0]
    steps_left = arr[0]

    for i in range(1, n):
        if i == n - 1:
            return jumps

        max_reach = max(max_reach, i + arr[i])
        steps_left -= 1

        if steps_left == 0:
            jumps += 1

            if i >= max_reach:
                return -1  

            steps_left = max_reach - i

    return -1 

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
result = min_jumps_to_reach_end(arr)
print(result)

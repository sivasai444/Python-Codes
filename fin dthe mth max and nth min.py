def find_mth_maximum_nth_minimum(arr, m, n):
    sorted_arr = sorted(arr, reverse=True)
    mth_maximum = sorted_arr[m - 1]
    
    sorted_arr = sorted(arr)
    nth_minimum = sorted_arr[n - 1]

    return mth_maximum, nth_minimum

array_of_elements = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3

mth_maximum, nth_minimum = find_mth_maximum_nth_minimum(array_of_elements, M, N)

sum_result = mth_maximum + nth_minimum
difference_result = mth_maximum - nth_minimum

print("Mth maximum:",mth_maximum)
print("Nth minimum:",nth_minimum)
print("Sum of Mth maximum and Nth minimum:",sum_result)
print("Difference of Mth maximum and Nth minimum:",difference_result)

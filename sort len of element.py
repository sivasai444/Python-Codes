def sort_by_length(input_list):
    return sorted(input_list,key=len)
my_list=["apple","banana","grape","orange"]
sorted_list=sort_by_length(my_list)
print(sorted_list)

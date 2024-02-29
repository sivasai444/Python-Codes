def calculate_user_details(total_users, staff_users):
    
    non_teaching_staff_users = staff_users // 3
    student_users = total_users - staff_users - non_teaching_staff_users

    return student_users, staff_users, non_teaching_staff_users

total_users = int(input("Total Users: "))
staff_users = int(input("Staff Users: "))

student_users, staff_users, non_teaching_staff_users = calculate_user_details(total_users, staff_users)
print(f"Student Users: {student_users}")
print(f"Staff Users: {staff_users}")
print(f"Non-teaching Staff Users: {non_teaching_staff_users}")

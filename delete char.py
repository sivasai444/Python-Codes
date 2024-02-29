def delchar(s, c):
    if len(c) != 1:
        return s

    result = ''.join(char for char in s if char != c)
    return result

input_string = input("Enter the string: ")
char_to_delete = input("Enter a character to be deleted: ")

output_string = delchar(input_string, char_to_delete)

print("String after the character is removed:", output_string)

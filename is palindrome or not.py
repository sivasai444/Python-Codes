def is_valid_palindrome(s):
    
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

    
    return cleaned_s == cleaned_s[::-1]


input_string = "A man, a plan, a canal, Panama!"
result = is_valid_palindrome(input_string)
print(result)

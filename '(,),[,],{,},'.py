def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

input_string = "[{()}]"
result = isValid(input_string)

if result:
    print("The input string is valid.")
else:
    print("The input string is not valid.")

    

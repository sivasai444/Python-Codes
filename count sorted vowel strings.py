def count_sorted_vowel_strings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    def count_strings_helper(length, last_vowel):
        if length == 0:
            return 1
        
        count = 0
        for vowel in vowels:
            if vowel >= last_vowel:
                count += count_strings_helper(length - 1, vowel)
        return count
    
    return count_strings_helper(n, '')

n = 1
result = count_sorted_vowel_strings(n)
print(result)

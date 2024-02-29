import re
def rem_vowel(string):
    return(re.sub("[aeiouAEIOU]","",string))
string=input("entre the string:")
x = rem_vowel(string)
print(x)

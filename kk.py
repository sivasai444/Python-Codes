string=input("enter the string:")
import re
def rem_vowel(string):
    return(re.sub("[aeiouAEIOU]","",string))
x=rem_vowel(string)
print(x)

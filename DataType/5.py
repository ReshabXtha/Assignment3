# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

print('Enter the text:')
Str = input()
x = len(Str)
if Str[x - 3:] == "ing":
    Str = Str + "ly"
    print(Str)
else:
    Str = Str + "ing"
    print(Str)

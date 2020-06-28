# 1)Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
str1 = 'google.com'
Str2 = {}
for n in str1:
    keys = Str2.keys()
    if n in keys:
        Str2[n] += 1
    else:
        Str2[n] = 1
print(Str2)



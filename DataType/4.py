# 4. Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
Str1 = 'abc'
Str2 = 'xyz'
Str3 = Str2[0:2] + Str1[2]
Str4 = Str1[0:2] + Str2[2]
print(Str3 + ' ' + Str4)

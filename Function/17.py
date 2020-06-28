#17. Write a Python program to find if a given string starts with a given character using Lambda.
str1="Reshab"
start_with=lambda x: True if x.startswith('R') else False
str2=start_with(str1)
print(str2)
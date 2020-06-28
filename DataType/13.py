# 13. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in
# sorted form (alphanumerically).
str = " red, white, black, red, green, black"
str1 = str.split(",")
str1.sort()
print(str1)

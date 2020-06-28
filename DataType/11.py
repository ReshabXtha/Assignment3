# 11. Write a Python program to count the occurrences of each word in a given sentence.
print('Enter the string:')
str = input()
count = dict()
words = str.split()
for i in words:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

# 7. Write a Python function that takes a list of words and returns the length of the longest one
word_list = ['banana', 'mango', 'apple', 'car', 'bike']
length = []
for x in word_list:
    length.append(len(x))
length.sort()
print(length[-1])
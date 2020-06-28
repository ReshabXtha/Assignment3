# 15. Write a Python function to insert a string in the middle of a string.
def insert_sting_middle(str1, str2):
    print(str1[:2] + str2 + str1[2:])


insert_sting_middle('[[]]', 'Python')
insert_sting_middle('{{}}', 'PHP')

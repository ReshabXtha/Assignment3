#14. Write a Python program to sort a list of dictionaries using Lambda.
lis=[
{"name": "Tom", "age": 10},
{"name": "Mark", "age": 5},
{"name": "Pam", "age": 7}
]
print(lis)
lis.sort(key=lambda x:x['age'])
print(lis)
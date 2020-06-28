# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unq(lis1):
    lis2 = []

    for i in lis1:
        if i not in lis2:
            lis2.append(i)
    print(lis2)


print("Enter the list=")
lis = list(input())
print(lis)
unq(lis)

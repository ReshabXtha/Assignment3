# 10. Write a Python program to print the even numbers from a given list.
def even(lis1):
    lis2 = []
    for x in lis1:
        if x % 2 == 0:
            lis2.append(x)
    print(lis2)


even([1, 2, 3, 4, 5, 6, 7, 8, 9])

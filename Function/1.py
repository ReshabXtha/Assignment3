# 1. Write a Python function to find the Max of three numbers.
def max_num(a, b, c):
    if a > b > c:
        print('Max number is', a)
    elif b > a > c:
        print('Max number is', b)
    else:
        print('Max number is', c)


print('Enter the first num=')
x = input()
print('Enter the second num=')
y = input()
print('Enter the third num=')
z = input()
max_num(x, y, z)

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def fact(n):
    if n < 0:
        return 'Negative number'
    elif n == 0:
        return 1
    else:
        fac = n * fact(n - 1)
        return fac


print('Enter the number=')
m = int(input())
print(fact(m))
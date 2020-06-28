# 6. Write a Python function to check whether a number is in a given range.
def check(n):
    if n in range(1, 100):
        return True
    else:
        return False


print('Enter the number=')
m = int(input())
print(check(m))

# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
def check_prime(n):
    if n > 1:
        if n % 2 == 0:
            return True
        else:
            return False
    else:
        return "Enter number greater than 1"


print("Enter the number=")
i = int(input())
print(check_prime(i))

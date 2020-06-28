# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def upper_lower(str2):
    d = {
        "Upper": 0,
        "lower": 0
    }
    for x in str2:
        if x.isupper():
            d["Upper"] = d["Upper"] + 1
        else:
            d["lower"] = d["lower"] + 1
    print(d)


print("Enter the text=")
str1 = input()
upper_lower(str1)

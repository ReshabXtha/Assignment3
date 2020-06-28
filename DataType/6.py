# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
def change(Str):
    x = Str.find('not')
    y = Str.find('poor')
    if y > x > 0:
        Str = Str.replace(Str[x:(y + 4)], 'good')
    print(Str)


change('The lyrics is not that poor!')
change('The lyrics is poor!')

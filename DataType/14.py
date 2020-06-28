# 14. Write a Python function to create the HTML string with tags around the word(s).
def add_tags(str1, str2):
    print('<' + str1 + '>' + str2 + '<' + str1 + '>')


add_tags('i', 'Python')
add_tags('b', 'Python Tutorial')

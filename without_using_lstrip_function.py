# removes the space at the beginning of the string
# results without the spaces at the beginning of the string

def manual_lstrip(string):
    for index in range(len(string)):
        if string[index] != ' ':
            return string[index:]
    return ''

string = input("Enter a string: ")
print(manual_lstrip(string))
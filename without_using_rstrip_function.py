# removes the space at the end of the string
# results without the spaces at the end of the string

def manual_rstrip(string):
    for index in range(len(string) - 1, -1, -1):
        if string[index] != ' ':
            return string[:index + 1]
    return ''

string = input("Enter a string: ")
print(manual_rstrip(string))
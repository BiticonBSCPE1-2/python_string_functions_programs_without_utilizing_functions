# capitalizes the first letter and lowers the rest
# results the string with the first letter capitalized and the rest in lowercase

def manual_capitalize(string):
    if not string:
        return ''
    first = chr(ord(string[0]) - 32) if 'a' <= string[0] <= 'z' else string[0]
    rest = ''.join(
        chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in string[1:])
    return first + rest

string = input("Enter a string: ")
print(manual_capitalize(string))
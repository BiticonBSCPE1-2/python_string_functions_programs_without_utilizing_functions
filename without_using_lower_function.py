# converts all characters to lowercase
# results with all characters in lowercase

def manual_lower(string):
    return ''.join(chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in string)

string = input("Enter a string: ")
print(manual_lower(string))
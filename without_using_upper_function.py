# converts all characters to uppercase
# results with all characters in uppercase

def manual_upper(string):
    return ''.join(
        chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in string)

string = input("Enter a string: ")
print(manual_upper(string))
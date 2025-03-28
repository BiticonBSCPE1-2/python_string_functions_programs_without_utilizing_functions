# swaps uppercase to lowercase and vice versa
# results the string with swapped cases

def manual_swapcase(string):
    return ''.join(
        chr(ord(char) + 32) if 'A' <= char <= 'Z' else
        chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        for char in string)

string = input("Enter a string: ")
print(manual_swapcase(string))
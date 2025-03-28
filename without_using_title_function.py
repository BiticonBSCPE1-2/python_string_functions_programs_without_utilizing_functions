# capitalizes the first letter of each word
# results the string with each word's first letter capitalized

def manual_title(string):
    result = ''
    for i in range(len(string)):
        if (i == 0 or string[i - 1] == ' ') and 'a' <= string[i] <= 'z':
            result += chr(ord(string[i]) - 32)
        elif (i != 0 and string[i - 1] != ' ') and 'A' <= string[i] <= 'Z':
            result += chr(ord(string[i]) + 32)
        else:
            result += string[i]
    return result

string = input("Enter a string: ")
print(manual_title(string))
# removes the matching prefix from the string
# results without the matching prefix from the string

def manual_removeprefix(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix):]
    return string

string = input("Enter a string: ")
prefix = input("Enter prefix to remove: ")
print(manual_removeprefix(string, prefix))
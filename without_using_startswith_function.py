# checks if the string starts with a particular prefix
# results True if the string starts with the prefix, False if not

def manual_startswith(string, prefix):
    if len(prefix) <= len(string):
        return string[:len(prefix)] == prefix
    return False

string = input("Enter a string: ")
prefix = input("Enter prefix to check: ")
print(manual_startswith(string, prefix))
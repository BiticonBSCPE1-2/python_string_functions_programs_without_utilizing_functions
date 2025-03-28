# checks if the string ends with a given suffix
# results True if the string ends with the given suffix, else False

def manual_endswith(string, suffix):
    if len(suffix) <= len(string):
        return string[-len(suffix):] == suffix
    return False

string = input("Enter a string: ")
suffix = input("Enter suffix to check: ")
print(manual_endswith(string, suffix))
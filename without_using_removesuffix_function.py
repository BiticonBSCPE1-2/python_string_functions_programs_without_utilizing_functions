# removes the suffix from the string
# results without the suffix from the string

def manual_removesuffix(string, suffix):
    if string.endswith(suffix):
        return string[:-len(suffix)]
    return string

string = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")
print(manual_removesuffix(string, suffix))
# checks if all characters are uppercase
# results True if all are uppercase, else False

def manual_isupper(string):
    return all(not ('a' <= char <= 'z') for char in string)

string = input("Enter a string: ")
print(manual_isupper(string))
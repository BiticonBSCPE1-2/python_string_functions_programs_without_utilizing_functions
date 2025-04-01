# checks if all characters are lowercase
# results True if all are lowercase, else False

def manual_islower(string):
    return all(not ('A' <= char <= 'Z') for char in string)

string = input("Enter a string: ")
print(manual_islower(string))
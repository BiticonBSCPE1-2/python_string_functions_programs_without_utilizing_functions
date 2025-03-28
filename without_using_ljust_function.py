# adds spaces to the right to make the string reach the given width
# results the string with added spaces at the right

def manual_ljust(string, width):
    return string + ' ' * max(0, width - len(string))

string = input("Enter a string: ")
width = int(input("Enter desired width: "))
print(manual_ljust(string, width))
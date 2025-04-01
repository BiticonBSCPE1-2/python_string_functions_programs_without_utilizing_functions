# adds spaces to the left to make the string reach the given width
# results the string with added spaces at the left

def manual_rjust(string, width):
    return ' ' * max(0, width - len(string)) + string

string = input("Enter a string: ")
width = int(input("Enter desired width: "))
print(manual_rjust(string, width))
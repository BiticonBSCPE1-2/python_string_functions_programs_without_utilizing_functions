# adds zeros to the left to make the string reach the given width
# results the string with added zeros at the left

def manual_zfill(string, width):
    return '0' * max(0, width - len(string)) + string

string = input("Enter a string: ")
width = int(input("Enter desired width: "))
print(manual_zfill(string, width))
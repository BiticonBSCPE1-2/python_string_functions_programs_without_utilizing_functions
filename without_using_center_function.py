# centers the string by adding spaces on both sides
# results the string at the center with added spaces at both sides

def manual_center(string, width):
    space = max(0, width - len(string))
    return ' ' * (space // 2) + string + ' ' * (space - space // 2)

string = input("Enter a string: ")
width = int(input("Enter desired width: "))
print(manual_center(string, width))
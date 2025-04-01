# finds the last occurrence of a substring
# results the position of the last occurrence

def manual_rindex(string, substring):
    for i in range(len(string) - len(substring), -1, -1):
        if string[i:i + len(substring)] == substring:
            return i
    return -1

string = input("Enter a string: ")
substring = input("Enter substring to find: ")
print(manual_rindex(string, substring))
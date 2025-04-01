# finds the first occurrence of a substring
# results the position of the first occurrence

def manual_index(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return i
    return -1

string = input("Enter a string: ")
substring = input("Enter substring to find: ")
print(manual_index(string, substring))
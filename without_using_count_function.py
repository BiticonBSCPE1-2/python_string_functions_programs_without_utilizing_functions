# counts occurrences of a substring in the string
# results the number of times the substring appears

def manual_count(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

string = input("Enter a string: ")
substring = input("Enter substring to count: ")
print(manual_count(string, substring))
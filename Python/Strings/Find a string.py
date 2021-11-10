def count_substring(string, sub_string):
    one_more_iteration, total = len(string) - len(sub_string), 0
    for i in range(0, len(string)):
        if i <= one_more_iteration:
            compare = string[i:i + len(sub_string)]
            if sub_string == compare:
                total += 1
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

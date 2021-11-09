def swap_case(s):
    my_str = list(s)
    for i, element in enumerate(my_str):
        if element.islower():
            my_str[i] = element.upper()
        elif element.isupper():
            my_str[i] = element.lower()
    return ''.join(my_str)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

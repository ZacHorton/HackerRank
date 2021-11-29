from collections import OrderedDict


def my_split(my_string):
    head = my_string.rstrip("0123456789").rstrip()
    tail = my_string[len(head) + 1:]
    my_list = [head, tail]
    return my_list


if __name__ == '__main__':
    ordered_dictionary = OrderedDict()

    n = int(input())
    for x in range(n):
        my_list = my_split(input())
        my_key = my_list[0]
        my_value = int(my_list[1])
        if my_key in ordered_dictionary.keys():
            ordered_dictionary[my_key] += int(my_value)
        else:
            ordered_dictionary[my_key] = my_value

    for key, value in ordered_dictionary.items():
        print(key, value)

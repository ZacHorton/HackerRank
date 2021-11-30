from itertools import combinations


def my_split(my_string):
    head = my_string.rstrip("0123456789").rstrip()
    tail = my_string[len(head) + 1:]
    my_list = [head, tail]
    return my_list


if __name__ == '__main__':
    user_input = input()
    my_list = my_split(user_input)
    my_str = my_list[0]
    my_int = int(my_list[1])
    my_list_sorted = []
    for i in range(my_int):
        comb = sorted(list(combinations(my_str, i + 1)))
        for x in comb:
            my_list_sorted.append(x)

    print(my_list_sorted)

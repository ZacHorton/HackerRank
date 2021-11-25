def average(array):
    my_set = set(array)
    len_set = len(my_set)
    sum_set = sum(my_set)
    return '{0:.3f}'.format(sum_set / len_set)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

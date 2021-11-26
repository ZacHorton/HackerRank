from collections import defaultdict


if __name__ == '__main__':
    nm = input().split(" ")
    n = int(nm[0])
    m = int(nm[1])
    list_a, list_b = [], []
    for i in range(n):
        list_a.append(input())
    for j in range(m):
        list_b.append(input())

    dd = defaultdict(list)
    for i in range(len(list_b)):
        for j in range(len(list_a)):
            if list_b[i] == list_a[j]:
                dd[list_b[i]].append(j + 1)
        if list_b[i] not in list_a:
            dd[list_b[i]].append(-1)
    for key, value in dd.items():
        for x in value:
            print(x, end=" ")
        print()

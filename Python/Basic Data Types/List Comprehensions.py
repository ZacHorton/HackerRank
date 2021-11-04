if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # multiple loops
    # my_lit = []
    # for x in range(x + 1):
    #    for y in range(y + 1):
    #        for z in range(z + 1):
    #            my_lit.append([x, y, z])
    # print(my_lit)

    # list comprehensions
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

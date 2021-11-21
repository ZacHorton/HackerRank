from itertools import product

if __name__ == '__main__':
    a = list(input().split(' '))
    b = list(input().split(' '))
    c = list(product(a, b))
    x = str(c).replace("), (", ") (")
    print(x[1:-1].replace("'", ""))

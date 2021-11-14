from string import ascii_lowercase


def print_rangoli(size):
    # Top
    rows, counter = size - 1, size - 1
    for x in reversed(range(rows)):
        dashes = '--' * (x + 1)
        print(dashes, end="")
        for e in reversed(ascii_lowercase[counter:size]):
            if x == rows - 1:
                print(e, end="")
                print(dashes)
            else:
                print(e, end="-")
        for f in ascii_lowercase[counter + 1:size]:
            if f == ascii_lowercase[size - 1]:
                print(f, end="")
                print(dashes)
            else:
                print(f, end="-")
        counter -= 1

    # Middle
    for c in reversed(ascii_lowercase[:size]):
        if size == 1:
            print(c)
        else:
            print(c, end="-")
    for d in ascii_lowercase[1:size]:
        if d == ascii_lowercase[size - 1]:
            print(d)
        else:
            print(d, end="-")

    # Bottom
    rows, counter = size - 1, 1
    for x in range(rows):
        dashes = '--' * counter
        print(dashes, end="")
        for e in reversed(ascii_lowercase[counter:size]):
            if x == rows - 1:
                print(e, end="")
                print(dashes)
            else:
                print(e, end="-")
        for f in ascii_lowercase[counter + 1:size]:
            if f == ascii_lowercase[size - 1]:
                print(f, end="")
                print(dashes)
            else:
                print(f, end="-")
        counter += 1


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

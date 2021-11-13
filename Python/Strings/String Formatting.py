def print_formatted(number):
    padding = len(bin(number)[2:])
    for x in range(1, number + 1):
        print(f"{str(x).rjust(padding)} {oct(x)[2:].rjust(padding)} {hex(x)[2:].upper().rjust(padding)} {bin(x)[2:].rjust(padding)}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

def handshake(n):
    sums = 0
    if n == 1 or n == 2:
        return n - 1
    else:
        for i in range(1, n):
            sums += i
    return sums

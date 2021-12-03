if __name__ == "__main__":
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    a_diff = a.difference(b)
    b_diff = b.difference(a)
    diffs = sorted(a_diff.union(b_diff))
    for x in diffs:
        print(x)

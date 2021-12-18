from itertools import groupby

if __name__ == "__main__":
    s = input()
    for key, group in (groupby(s)):
        print(f"({len(list(group))}, {key})", end=" ")

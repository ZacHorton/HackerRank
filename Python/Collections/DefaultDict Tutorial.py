from collections import defaultdict

if __name__ == "__main__":
    user_input = list(map(int, input().split()))
    n = user_input[0]
    m = user_input[1]
    group_a = [input() for i in range(n)]
    group_b = [input() for i in range(m)]
    d = defaultdict(list)
    for i, x in enumerate(group_a):
        d[x].append(i + 1)
    d.default_factory = lambda: [-1]
    for x in group_b:
        print(*(d[x]))
        

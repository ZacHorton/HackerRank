if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        try:
            l = list(map(int, input().split()))
            print(l[0] // l[1])
        except (ZeroDivisionError, ValueError) as e:
            print(f"Error Code: {e}")
            

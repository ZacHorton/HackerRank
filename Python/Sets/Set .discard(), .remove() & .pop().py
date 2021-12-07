if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for x in range(N):
        user_input = input().split()
        """operation = user_input[0]
        element = user_input[1]"""
        if len(user_input) == 1:
            s.pop()
        else:
            operation = user_input[0]
            element = int(user_input[1])
            if operation == "remove":
                s.remove(element)
            else:
                s.discard(element)
    sum = 0
    for element in s:
        sum += element
    print(sum)
    

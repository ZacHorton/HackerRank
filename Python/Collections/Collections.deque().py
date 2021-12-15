from collections import deque

if __name__ == "__main__":
    num_of_ops = int(input())
    d = deque()
    for i in range(num_of_ops):
        user_input = list(map(str, input().split()))
        if user_input[0] == 'append':
            x = int(user_input[1])
            d.append(x)
        elif user_input[0] == 'pop':
            d.pop()
        elif user_input[0] == 'popleft':
            d.popleft()
        elif user_input[0] == 'appendleft':
            x = int(user_input[1])
            d.appendleft(x)
    for element in d:
        print(element, end=" ")
    

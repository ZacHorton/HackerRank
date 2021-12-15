if __name__ == "__main__":
    set_a = set(map(int, input().split()))
    num_of_supersets = int(input())
    answer = True
    for i in range(num_of_supersets):
        set_b = set(map(int, input().split()))
        for element in set_b:
            if element not in set_a:
                answer = False
    print(answer)
    

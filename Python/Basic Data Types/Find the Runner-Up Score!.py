if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(arr)
    winner = sorted_arr[-1]
    runner_up_arr = []
    for x in sorted_arr:
        if x != winner:
            runner_up_arr.append(x)
    runner_up = runner_up_arr[-1]
    print(runner_up)
    

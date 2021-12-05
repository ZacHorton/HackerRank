from itertools import combinations_with_replacement

if __name__ == "__main__":
    user_input = input().split()
    s = sorted(user_input[0])
    k = int(user_input[1])
    combo = list((combinations_with_replacement(s, k)))
    for x in combo:
        for y in x:
            print(y, end="")
        print()
        

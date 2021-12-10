if __name__ == "__main__":
    n = int(input())
    english_set = set(map(int, input().split()))
    b = int(input())
    french_set = set(map(int, input().split()))
    diff_set = english_set.difference(french_set)
    print(len(diff_set))
    

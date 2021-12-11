if __name__ == "__main__":
    n = int(input())
    english_set = set(map(int, input().split()))
    b = int(input())
    french_set = set(map(int, input().split()))
    symm_diff_set = english_set.symmetric_difference(french_set)
    print(len(symm_diff_set))
    

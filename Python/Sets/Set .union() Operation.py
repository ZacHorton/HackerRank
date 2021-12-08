if __name__ == "__main__":
    n = int(input())
    english_set = set(map(int, input().split()))
    b = int(input())
    french_set = set(map(int, input().split()))

    combo_set = english_set.union(french_set)
    print(len(combo_set))
    

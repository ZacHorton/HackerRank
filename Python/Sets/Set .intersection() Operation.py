if __name__ == "__main__":
    n = int(input())
    english_set = set(map(int, input().split()))
    b = int(input())
    french_set = set(map(int, input().split()))
    intersection_set = english_set.intersection(french_set)
    print(len(intersection_set))
    

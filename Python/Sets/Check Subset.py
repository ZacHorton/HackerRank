if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        len_set_a = int(input())
        set_a = set(map(int, input().split()))
        len_set_b = int(input())
        set_b = set(map(int, input().split()))
        set_test = set()

        for element in set_a:
            if element in set_b:
                set_test.add(element)

        if set_a == set_test:
            print("True")
        else:
            print("False")
            

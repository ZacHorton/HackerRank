if __name__ == "__main__":
    num_of_a = int(input())
    set_of_a = set(input().split())
    num_of_other = int(input())
    for i in range(num_of_other):
        function_nums = input().split()
        function = function_nums[0]
        nums = function_nums[1]
        other_set = set(input().split())
        if function == "update":
            set_of_a.update(other_set)
        elif function == "intersection_update":
            set_of_a.intersection_update(other_set)
        elif function == "difference_update":
            set_of_a.difference_update(other_set)
        elif function == "symmetric_difference_update":
            set_of_a.symmetric_difference_update(other_set)
    sum_of_a = 0
    for x in set_of_a:
        sum_of_a += int(x)
    print(sum_of_a)
    

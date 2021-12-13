if __name__ == "__main__":
    size_of_group = int(input())
    list_of_room_nums = list(map(int, input().split()))
    sorted_list_of_room_nums = sorted(list_of_room_nums)
    set_of_room_nums = set(list_of_room_nums)
    print(set_of_room_nums)
    for x in set_of_room_nums:
        print(x)
        print(sorted_list_of_room_nums.count(x))
        print(size_of_group)
        if sorted_list_of_room_nums.count(x) is not size_of_group:
            print(f"answer: {x}")
            break

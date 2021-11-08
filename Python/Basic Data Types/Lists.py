# The first example has the wrong output:
# "insert i e: Insert integer e at position i."
# 	insert(index, integer)
# "insert 3 1: Insert 3 at index 1"
# 	insert(integer, index)

if __name__ == "__main__":
    N = int(input())
    my_list = []
    for x in range(N):
        command = str(input())
        if "insert " in command:
            my_str = command
            my_nums = my_str.replace("insert ", "")
            my_pos, my_int = my_nums.split(" ", 1)
            my_list.insert(int(my_pos), int(my_int))
        elif command == "print":
            print(my_list)
        elif "remove " in command:
            my_str = command
            my_num = int(my_str.replace("remove ", ""))
            if my_num in my_list:
                my_list.remove(my_num)
        elif "append " in command:
            my_str = command
            my_num = int(my_str.replace("append ", ""))
            my_list.append(my_num)
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()
        else:
            print("Unrecognized command. ")

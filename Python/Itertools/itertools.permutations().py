from itertools import permutations


if __name__ == "__main__":
    user_input = input().split(' ')
    if int(user_input[1]) == 0:
        print()
    elif int(user_input[1]) == 1:
        for letter in user_input[0]:
            print(letter)
    else:
        output = list(permutations(user_input[0], int(user_input[1])))
        sorted_output = sorted(output)
        for x in sorted_output:
            for letter in x:
                print(letter, end="")
            print()

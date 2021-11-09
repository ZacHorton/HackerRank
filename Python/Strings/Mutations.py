def mutate_string(string, position, character):
    arr = list(string)
    arr[position] = character
    new_str = "".join(arr)
    return new_str
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

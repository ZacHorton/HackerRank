from collections import Counter


def minion_game(string):
    # Create list with every substring including repeats using list comprehension and string slicing
    # Credit GeeksForGeeks.org
    res = [string[i: j] for i in range(len(string))
           for j in range(i + 1, len(string) + 1)]

    vowels = "AEIOU"
    kevin_list = []
    stuart_list = []
    for i, x in enumerate(res):
        if x[0] in vowels:
            kevin_list.append(x)
        else:
            stuart_list.append(x)
    stuart_dict = Counter(stuart_list)
    kevin_dict = Counter(kevin_list)

    # Counter.total() is new in version 3.10 but HackerRank creates Runtime Error
    # stuart_score = stuart_dict.total()
    # kevin_score = kevin_dict.total()

    stuart_score, kevin_score = 0, 0
    for key, value in stuart_dict.items():
        stuart_score += value
    for key, value in kevin_dict.items():
        kevin_score += value

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif stuart_score < kevin_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)

if __name__ == "__main__":
    s = input()
    for x in s:
        if x.isalnum():
            print("True")
            break
    else:
        print("False")

    for x in s:
        if x.isalpha():
            print("True")
            break
    else:
        print("False")

    for x in s:
        if x.isdigit():
            print("True")
            break
    else:
        print("False")

    for x in s:
        if x.islower():
            print("True")
            break
    else:
        print("False")

    for x in s:
        if x.isupper():
            print("True")
            break
    else:
        print("False")

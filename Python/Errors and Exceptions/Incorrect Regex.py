import re

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        try:
            re.compile(s)
        except:
            print("False")
        else:
            print("True")
        

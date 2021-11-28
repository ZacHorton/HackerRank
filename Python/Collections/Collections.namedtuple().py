from collections import namedtuple


if __name__ == "__main":
    n = input()
    column_names = input().split("\t")
    for i, x in enumerate(column_names):
        if x == "MARKS":
            marks = column_names[i]
    Student = namedtuple('Student', 'ID MARKS NAME CLASS')

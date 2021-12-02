if __name__ == "__main__":
    n = int(input())
    column_names = input().split()
    marks_index = column_names.index("MARKS")
    total = 0
    for x in range(n):
        data = input().split()
        student_marks = int(data[marks_index])
        total += student_marks
    print('{0:.2f}'.format(total / n))
    

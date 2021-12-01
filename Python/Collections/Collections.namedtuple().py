if __name__ == "__main__":
    n = int(input())
    column_names, total, marks = input().split(), 0, 0
    for i, x in enumerate(column_names):
        if x == "MARKS":
            marks = i
    for x in range(n):
        data = input().split()
        total += int(data[marks])
    print('{0:.2f}'.format(total / n))
    

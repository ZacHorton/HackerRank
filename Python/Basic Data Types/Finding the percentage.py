if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for n, m in student_marks.items():
        if query_name == n:
            sums, count = 0, 0
            for x in m:
                sums += x
                count += 1
            avg = "{:.2f}".format(sums / count)
            print(avg)

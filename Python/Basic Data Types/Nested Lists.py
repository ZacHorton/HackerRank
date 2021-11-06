if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    grades = []
    for x in records:
        for y in range(1, 2):
            grades.append(x[1])
    sorted_grades = sorted(grades)
    lowest_grade = sorted_grades[0]

    new_arr = []
    for x in sorted_grades:
        if x != lowest_grade:
            new_arr.append(x)

    second_lowest_grade = new_arr[0]
    names = []
    for x in records:
        for y in range(1, 2):
            if x[1] == second_lowest_grade:
                names.append(x[0])
    sorted_names = sorted(names)

    for x in sorted_names:
        print(x)

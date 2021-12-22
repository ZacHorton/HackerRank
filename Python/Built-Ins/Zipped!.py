if __name__ == "__main__":
  nx = list(map(int, input().split()))
  n = nx[0]
  x = nx[1]
  subjects = []
  for i in range(x):
    subject = list(map(float, input().split()))
    subjects.append(subject)
  students = zip(*subjects)
  total = 0
  for student in students:
    for grades in student:
      total += grades
    average = total / x
    print("{:.1f}".format(average))
    total = 0
  

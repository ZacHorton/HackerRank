import datetime

if __name__ == "__main__":
  T = int(input())
  for i in range(T):
    x1 = datetime.datetime.strptime(input(), '%a %d %b %Y %X %z')
    x2 = datetime.datetime.strptime(input(), '%a %d %b %Y %X %z')
    if x1 > x2:
      return_value = (x1 - x2).total_seconds()
      print(int(return_value))
    else:
      return_value = (x2 - x1).total_seconds()
      print(int(return_value))

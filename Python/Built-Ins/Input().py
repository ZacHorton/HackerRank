if __name__ == '__main__':
  x, k = map(int, input().split())
  P = input()
  answer = eval(P)
  if k == answer:
    print('True')
  else:
    print('False')
  

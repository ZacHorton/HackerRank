if __name__ == '__main__':
  n, m = input().split()
  n_arr = list(map(int, input().split()))
  a_set = set(map(int, input().split()))
  b_set = set(map(int, input().split()))
  happiness = 0

  for element in n_arr:
    if element in a_set:
      happiness += 1
    if element in b_set:
      happiness -= 1
  
  print(happiness)

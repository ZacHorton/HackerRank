from itertools import product

if __name__ == '__main__':
  a = [5, 4]
  b = [7, 8, 9 ]
  c = [5, 7, 8, 9, 10 ]
  K, M = map(int, input().split())
  ilist = []
  for i in range(K):
    elements = list(map(int, input().split()))
    ilist.append(elements[1:])
  combos = list((product(*ilist)))
  total, mod, solution = 0, 0, 0
  for x in combos:
    for y in x:
      total += y**2
    mod = total % M
    if mod > solution:
      solution = mod
    total, mod = 0, 0
  print(solution)

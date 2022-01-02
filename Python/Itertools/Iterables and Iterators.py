from itertools import combinations

if __name__ == "__main__":
  N = int(input())
  elements = input().split()
  K = int(input())
  combos = list(combinations(elements, K))
  count = 0
  for x in combos:
    if "a" in x:
      count += 1
  result = count / len(combos)
  print("{:.4f}".format(result))
  

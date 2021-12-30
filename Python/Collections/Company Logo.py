from collections import Counter

if __name__ == "__main__":
  d = Counter(list(sorted(input())))
  for char in d.most_common(3):
    print(*char)
  

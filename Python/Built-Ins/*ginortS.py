# stefan_pochmann on HackerRank

if __name__ == "__main__":
  print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

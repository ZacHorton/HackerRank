from collections import deque

if __name__ == "__main__":
  T = int(input())
  for i in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))
    stack = 2**31
    continues = True
    while continues:
      left = blocks[0]
      right = blocks[-1]
      if len(blocks) == 1 and left <= stack:
        print("Yes")
        continues = False  
      elif left > right and left <= stack:
        largest = left
        stack = blocks.popleft()
      elif left < right and right <= stack:
        largest = right
        stack = blocks.pop()
      elif left == right and left <= stack:
        blocks.pop()
        stack = blocks.popleft()
      else:
        print("No")
        continues = False
  

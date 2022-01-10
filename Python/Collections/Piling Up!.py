from collections import deque

if __name__ == "__main__":
  T = int(input())
  for i in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))
    last = 2 ** 31
    for j in range(n):
      answer = "Unknown"
      left = blocks[0]
      right = blocks[-1]
      if len(blocks) != 1 and left >= right:
        last = left
        blocks.popleft()
      elif left < right and last >= right:
        last = right
        blocks.pop()
      elif len(blocks) == 1:
        if left > last:
          answer = "No"
          print(answer)
        elif left <= last:
          answer = "Yes"
          print(answer)
      elif len(blocks) != 1:
          answer = "No"
          print(answer)
          break
  

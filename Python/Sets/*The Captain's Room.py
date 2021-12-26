from collections import Counter

if __name__ == "__main__":
  K = int(input())
  room_number_list = list(map(int, input().split()))
  c = Counter(room_number_list)
  for key, value in c.items():
      if value == 1:
        print(key)
  

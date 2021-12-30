from collections import Counter

if __name__ == "__main__":
  n = int(input())
  words = []
  for x in range(n):
    word = input()
    words.append(word)
  count_words = Counter(words)
  print(len(count_words))
  for y in count_words.values():
    print(y, end=" ")
   

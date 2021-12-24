if __name__ == "__main__":
  N = int(input())
  list_of_N = list(map(int, input().split()))
  list_of_bool_1 = []
  list_of_bool_2 = [] 

  for x in list_of_N:
    list_of_bool_1.append(x > 0)
  for x in list_of_N:
    list_of_bool_2.append(str(x) == str(x)[::-1])

  if all(list_of_bool_1):
    if any(list_of_bool_2):
      print("True")
    else:
      print("False")
  else:
    print("False")
  

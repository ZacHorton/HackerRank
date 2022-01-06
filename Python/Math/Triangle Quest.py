x, y = 1, 1
for i in range(1, int(input())): 
    print(i * x)
    y *= 10
    x += y

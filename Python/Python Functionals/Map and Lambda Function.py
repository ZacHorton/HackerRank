cube = lambda x: x**3  

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    arr = [0, 1]
    index_1 = 0
    index_2 = 1
    for i in range(n-2):
        arr.append(arr[index_1] + arr[index_2])
        index_1 += 1
        index_2 += 1
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

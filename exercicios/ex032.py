
while True:
    n = int(input())
        
    if n == -1:
        break
    for _ in range(999):
        x = int(input())
        c += x == n
    print(f'{n} appeared {c} times')
    
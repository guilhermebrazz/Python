contador = 0
x = int(input())
for i in range(1, x + 1):
    if i % x == 0:
        contador += 1
    print(i)
print()
a, b = map(int, input().split())

multiplos = []

for i in range(a, b + 1):
    if i % 5 == 0:
        multiplos.append(str(i))

print('|'.join(multiplos))
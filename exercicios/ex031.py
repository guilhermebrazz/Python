n = int(input())
c = 0
for i in range(20):
    s = int(input())
    
    if s == -1:
        break
    c += s == n
print(f'{n} aparece {c} vezes')

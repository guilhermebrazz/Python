a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('*')
elif a == b and b != c:
     print ('C')
elif b == c and c != a:
    print('A')
else:
    print('B')
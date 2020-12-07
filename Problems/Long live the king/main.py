x = int(input())
y = int(input())

if x == 1:
    if y == 1 or y == 8:
        print(3)
    elif y < 8:
        print(5)
elif x == 8:
    if y == 1 or y == 8:
        print(3)
    elif y < 8:
        print(5)
elif 1 < x < 8 and 1 < y < 8:
    print(8)
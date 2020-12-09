# put your python code here

y = 0
z = 0

while True:
    x = int(input())
    if x == 0 and y == 0:
        print(0)
        break
    y += x
    z += x ** 2
    if y == 0:
        print(z)
        break

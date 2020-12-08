# put your python code here

a = int(input())
b = int(input())
y = 0
z = 0

for x in range(a, b + 1):
    if x % 3 == 0:
        y += x
        z += 1

print(y / z)
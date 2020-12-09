y = 0
z = 0

while True:
    x = input()
    if x == ".":
        break
    y += int(x)
    z += 1

print(y / z)
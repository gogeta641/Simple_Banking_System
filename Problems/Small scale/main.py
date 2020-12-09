y = []

while True:
    x = input()
    if x == ".":
        break
    else:
        y.append(float(x))

print(min(y))
offset = int(input())

base = 10.5

if offset + base >= 24.0:
    print("Wednesday")
elif offset + base <= 0:
    print("Monday")
else:
    print("Tuesday")
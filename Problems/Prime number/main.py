number = int(input())

x = 0

for no in range(2, number):
    if number % no == 0:
        x = 1
    if number % no == 0:
        print("This number is not prime")
        break

if number == 1:
    print("This number is not prime")
elif x == 0:
    print("This number is prime")
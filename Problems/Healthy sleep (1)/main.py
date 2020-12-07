A = int(input())
B = int(input())
H = int(input())

if H < A:
    print("Deficiency")
elif A <= H <= B:
    print("Normal")
elif H > B:
    print("Excess")
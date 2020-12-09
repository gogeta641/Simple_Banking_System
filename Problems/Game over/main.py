scores = input().split()
# put your python code here

correct = 0
incorrect = 0

for score in scores:
    if score == "C":
        correct += 1
    else:
        incorrect += 1
    if incorrect == 3:
        break

if incorrect < 3:
    print("You won")
else:
    print("Game over")

print(correct)
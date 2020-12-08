army = int(input())

if army < 1:
    quote = "no army"
elif army <= 9:
    quote = "few"
elif army <= 49:
    quote = "pack"
elif army <= 499:
    quote = "horde"
elif army <= 999:
    quote = "swarm"
else:
    quote = "legion"

print(quote)
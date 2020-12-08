string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

x = 0

for y in string:
    if y in vowels:
        x += 1

print(x)

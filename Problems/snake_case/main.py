word = input()

first_letter = word[0].lower()

output_word = ""

for x in range(1, len(word)):
    if word[x].islower():
        output_word = output_word + word[x]
    else:
        output_word = output_word + "_" + word[x].lower()

print(first_letter + output_word)

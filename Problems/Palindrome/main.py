word = input()

length = len(word)

rev_length = -len(word) - 1

word_reversed = ""

for x in range(-1, rev_length, -1):
    word_reversed += word[x]

if word == word_reversed:
    print("Palindrome")
else:
    print("Not palindrome")
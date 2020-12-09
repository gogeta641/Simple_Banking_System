word = input().lower()
vowel = ["a", "e", "i", "o", "u"]

for x in word:
    if x in vowel:
        print("vowel")
    elif not x.isalpha():
        break
    else:
        print("consonant")
# Prompt the user to enter a word
# and assign it to the user_word variable.

# for letter in user_word:
    # Complete the body of the for loop.
word_without_vowels = ""

user_word = input()

user_word = user_word.upper()

for word in user_word:
    if word == "A":
        continue
    elif word == "E":
        continue
    elif word == "I":
        continue
    elif word == "O":
        continue
    elif word == "U":
        continue
    # print (word)
    word_without_vowels += word

print (word_without_vowels)
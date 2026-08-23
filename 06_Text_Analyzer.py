sentence = input("Enter your sentence: ")

sentence = sentence.strip().capitalize()

print(f"Cleaned sentence: {sentence}")
print(f"Character count: {len(sentence)}")

word = input("Enter a word to search for: ")

if word in sentence:
    print(f"{word} was found in the sentence!")
else:
    print(f"{word} wasn't found in the sentence!")
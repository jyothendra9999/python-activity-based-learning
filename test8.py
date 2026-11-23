# Sample Input:
# Enter a sentence: This is good and this is easy
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
shown = []
for word in words:
    if words.count(word) > 1 and word not in shown:
        print(word, "appears", words.count(word), "times")
        shown.append(word)
if len(shown) == 0:
    print("No repeated words")
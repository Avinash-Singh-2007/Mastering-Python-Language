def remove_word(words, word):
    n = []

    for w in words:
        if not (word == w):
            n.append(w.strip(word))
    return n

lst = ["apple", "banana", "apple", "orange","le"]
print(remove_word(lst, "le"))

# WAP for function to remove a given word from a list and strip it at the same time.
def rem(l, word):
    n = []
    for item in l:
        if item != word:
            # Remove the word as a substring and strip whitespace
            cleaned = item.replace(word, "").strip()
            n.append(cleaned)
    return n

l = ["Ishant", "Raj", "Rohan", "an"]
print(rem(l, "an"))  # Output: ['Ishant', 'Raj', 'Rohan']

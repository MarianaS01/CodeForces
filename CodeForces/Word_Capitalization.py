# Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.
# Note, that during capitalization all the letters except the first one remains unchanged.

def capitalization(word):
    first = word[0].upper()
    capitalized = first + word[1:]
    return capitalized

print(capitalization('apPLe'))    
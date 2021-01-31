#  For example, the word HoUse must be replaced with house, and the word ViP — with VIP. If a word contains an equal number of uppercase and lowercase letters, you should replace all the letters with lowercase ones. For example, maTRIx should be replaced by matrix. Your task is to use the given method on one given word.

def word(word):
    lower = 0

    for l in word:
        if l == l.lower():
            lower += 1

    if lower > len(word)-lower:
        return word.lower()
    elif lower < len(word)-lower:
        return word.upper()    
    elif lower == len(word)-lower:
        return word.lower()    

print(word('maTRIx'))            

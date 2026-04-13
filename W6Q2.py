text = 'Hello cruel world'
banned_words = {'Hello', 'world'}

def censor_words(text,banned_words):
    new_text = ''
    words = text.split()
    for w in words:
        if w not in banned_words:
            new_text += w + ' '
        else:
            new_text += '*' * len(w) + ' '
    return new_text

print(censor_words(text,banned_words))
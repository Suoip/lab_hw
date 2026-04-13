text = 'Hello cruel world'
banned_words = {'Hello', 'world'}
words = text.split()
new_text = ''
for w in words:
    if w not in banned_words:
        new_text += w

print(new_text)
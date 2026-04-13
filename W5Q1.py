sentence = str(input('Input your sentence: '))
words_list = sentence.split()
words_count = {}
for word in words_list:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
sorted_count = sorted(words_count.items())
sorted_count.sort(key=lambda x: x[1], reverse=True)
print(sorted_count[:3])
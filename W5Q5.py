dict_count = {'Sude':90,'Salih':70,'Baver':80}


sorted_count = sorted(dict_count.items())
sorted_count.sort(key=lambda x: x[1], reverse=True)
for name,score in sorted_count:
    print(name,score)
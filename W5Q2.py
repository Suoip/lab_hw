first_text = 'Hello World!'
second_text = 'Hello Dünya!'

first_set = set(first_text.split())
second_set = set(second_text.split())

intersection = first_set.intersection(second_set)

print(intersection)
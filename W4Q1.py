students = []

while True:
    name = input('Name(to exit input q):').strip()
    if name.lower() == 'q':
        print('\n')
        break
    if not name:
        continue
    note = input('Grade(0-100): ').strip()
    if not note.isdigit():
        continue
    grade = int(note)
    if not(0<=grade<=100):
        continue
    students.append((name,grade))
lowest_name = students[0][0]
lowest = students[0][1]
hightest_name = students[0][0]
hightest = students[0][1]
sum = 0
students.sort()
for name,grade in students:
    print(f'{name}:{grade}')
for name,grade in students:
    if grade < lowest:
        lowest = grade
        lowest_name = name
for name,grade in students:
    if grade > lowest:
        hightest = grade
        hightest_name = name

for name,grade in students:
    sum += grade

average = sum/len(students)

print(f'\nLowest person is {lowest_name} with a score of {lowest} \n\nHighest person is {hightest_name} with a score of {hightest} \n\nThe average grade is {average}\n')
    
        
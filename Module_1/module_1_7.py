grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def average(data):
    return [sum(obj) / len(obj) if len(obj) > 0 else 0 for obj in data]
students_and_average_grades = dict(zip(sorted(students), average(grades)))
print(students_and_average_grades)


def func(data):
    res = []
    for obj in data:
        value = sum(obj) / len(obj)
        res.append(value)
    return res
print(dict(zip(sorted(students), func(grades))))


average_grades = []
for obj in grades:
    s = sum(obj)/len(obj)
    average_grades.append(s)
print(average_grades)
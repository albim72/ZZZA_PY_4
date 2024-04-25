from homework import Homework
from exam import Exam

print("____________ HOMEWORK _______________")
s1 = Homework()
s1.grade = 97
assert s1.grade == 97
print(f'ocena: {s1.grade}')


print("____________ EXAM _______________")
s2 = Exam()
s2.writing_grade=88
s2.math_grade=75

print(f'oceny -> writing: {s2.writing_grade}, math: {s2.math_grade}')

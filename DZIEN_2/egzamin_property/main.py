from homework import Homework
from exam import Exam
from grade import ExamD

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

print("____________ EXAMD _______________")

s3f = ExamD()
s3f.math_grade = 34
s3f.writing_grade = 55
s3f.science_grade = 43
print(f"pierwsze podejście\nmath:{s3f.math_grade}\nwriting:{s3f.writing_grade}\nscience:{s3f.science_grade}")
print("__________________________________")
s3s = ExamD()
s3s.math_grade = 77
s3s.writing_grade = 65
s3s.science_grade = 89
print(f"drugie podejście\nmath:{s3s.math_grade}\nwriting:{s3s.writing_grade}\nscience:{s3s.science_grade}")
print("__________________________________")
print(f"ARCHIWUM:pierwsze podejście\nmath:{s3f.math_grade}\nwriting:{s3f.writing_grade}\nscience:{s3f.science_grade}")
print(s3f==s3s)
print(s3f.math_grade == s3s.math_grade)

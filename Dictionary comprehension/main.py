# how to make dictionary comprehensions
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# dictionary exercise on students:
import random
names = {'Alex', 'Beth', 'Caroline', "Dave", 'Eleanor', 'Freddie'}

student_scores = {student: random.randint(1,100) for student in names}
# in here we have added a score to each of the students, therefore we have edited the list and converted into a dictionary
print(student_scores)

# now let's loop through a dictionary and check which of the students have passed:
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

# this would be the long way to create a new dictionary:
#passed_students = {}
#for student, score in student_scores.items():
    #if score > 60:
        #passed_students[student] = score

print(passed_students)
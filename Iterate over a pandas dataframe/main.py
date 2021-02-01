student_dict = {"student": ['Angela', 'James', 'Lily'],
                'score': [56, 76, 98]}

# Looping through dictionaries
#for (key,value) in student_dict.items():
    #print(value)

import pandas

student_df = pandas.DataFrame(student_dict)
#print(student_df)

# how to loop through a data frame, we're going to iterate for each of the rows
for (index, row) in student_df.iterrows():
    #I can print the index
    #print(index)
    # or I can print the row
    # print(row)
    # if I want to print something individually I can do:
    print(row.student)
    # or I can print the score of each student
    print(row.score)

# how to loop through a data frame, we're going to iterate for each of the rows but with conditionals
for (index, row) in student_df.iterrows():
    if row.student == 'Angela':
        print(row.score)
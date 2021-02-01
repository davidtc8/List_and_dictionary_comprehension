numbers = [1,2,3]

new_numbers = [n + 1 for n in numbers]

name = 'David'

new_list = [letter for letter in name]

r = range(1,5)

double_r = [number * 2 for number in r]
# you can also create the following by doing:

range_list = [number * 2 for number in range(5)]

range_list = [number * 2 for number in range(1,5)]
#in this case, we have created the same result, both double_r and range_list have the same values

# Working with conditional lists comprehensions:
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
#names
#['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

#let's say for instance that I want a new list that only has names with 4 letters or less
short_names = [name for name in names if len(name) <= 4]
all_caps = [name.upper() for name in names if len(name) > 5]

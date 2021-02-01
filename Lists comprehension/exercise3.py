# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers,
# each number on a new line.

# You are going to create a list called result which contains the numbers that
# are common in both files.
# new_list = [new_item for item in list]

with open(file = "file1.txt", mode = 'r') as file:
    content = file.readlines()
    list1 = [int(num) for num in content]

with open(file = "file2.txt", mode = 'r') as file:
    content = file.readlines()
    list2 = [int(num) for num in content]

result = [num for num in list1 for num2 in list2 if num == num2]

# you can also do the exercise by doing:
# result [num for num in list1 if num in list2]

#result = []

#for num in list1:
    #for num2 in list2:
        #if num == num2:
            #result.append(num)

# Write your code above 👆

print(result)
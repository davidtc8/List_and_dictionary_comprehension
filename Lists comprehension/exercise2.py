numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:
# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
# new_list = [new_item for item in list]

result = [num for num in numbers if num % 2 == 0]

#Write your code 👆 above:

print(result)
# You are going to use Dictionary Comprehension to create a dictionary called result that
# takes each word in the given sentence and calculates the number of letters in each word.
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
list_of_words = [words for words in sentence.split()]
result = {words: len(words) for words in list_of_words}
# Write your code below:

print(result)

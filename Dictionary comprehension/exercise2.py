# You are going to use Dictionary Comprehension to create a dictionary called
# weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f = {key: (value * 9/5) + 32 for (key,value) in weather_c.items()}

print(weather_f)
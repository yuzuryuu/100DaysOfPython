# Excercise 2 - BMI Calculator
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


bmi = int(weight) / (float(height)**2)
print(int(bmi))

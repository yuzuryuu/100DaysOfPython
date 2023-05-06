# Day 2 Project - Tip Calculator

totalBill = input("How much was the bill?\n$")
people = input("\nHow many people to split the bill?\n")
tip = input("\nHow much tip would you like to give?\n")
tipPercent = int(tip) / 100

splitBill = float(totalBill) / int(people)
eachPersonBill = (float(splitBill) * (float(tipPercent)+1))

print(f"\nEach person should pay: ${eachPersonBill:.2f}")

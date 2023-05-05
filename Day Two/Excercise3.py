# Exercise 3 - Life in Weeks
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

age = input("What is your current age? ")

months = (1080 - (int(age) * 12))
weeks = (4680 - (int(age) * 52))
days = (32850 - (int(age) * 365))

print("You have " + str(days) + " days, " + str(weeks) +
      " weeks, and " + str(months) + " months left.")
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

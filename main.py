print("Hello, Micky 👋")
name="Micky"
age=25
print("Name:", name)
print("Age:", age)
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

surname=input("Please enter your surname: ")
print("Your full name is:", name, surname)
updated_age = input("Please enter your updated age: ")
try:
    updated_age = int(updated_age)
    print("Your updated age is:", updated_age)
except ValueError:
    print("Invalid input for age. Please enter a number.")
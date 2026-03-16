print("Task 1: Variables and Data Types\n")

name = "Samuel Spitler"
age = 23
heightInMeters = 1.778
favProgrammingLanguage = "Python"
yrsCodingExperience = 2
currentlyLearningPython = True

print(f"=== Personal Information === \n Name: {name} \n Age: {age} \n Height: {heightInMeters} \n Favorite Programming Language: {favProgrammingLanguage} \n Years of Coding Experience: {yrsCodingExperience} \n Currently Learning Python: {currentlyLearningPython}\n")

print(type(name))
print(type(age))
print(type(heightInMeters))
print(type(favProgrammingLanguage))
print(type(yrsCodingExperience))
print(type(currentlyLearningPython))

print("\nTask 2: f-strings Practice\n")

prodName = "Wireless Mouse"
price = 29.99
quantity = 5
discount = 0.9
discountPercent = 10
discountAmount = price - (price * discount)
priceAfterDiscount = price * discount
print("=== Receipt ===\n")

print(f"{prodName}.....{price}\n		QTY: {quantity}\nSubtotal: {price}\nDiscount: {discountPercent}%\nDiscount Amount: {discountAmount:.2f}\nTotal: {priceAfterDiscount:.2f}")

print("\nTask 3: User Input and Type Conversion\n")

firstName = input("What is your first name? \n")
lastName = input("What is your last name? \n")
birthYear = int(input("What year were you born? \n"))
age = 2026 - birthYear
favNum = int(input("What is your favorite number? \n"))

print(f"{firstName} {lastName} is {age} years old and their favorite number is {int(favNum*2)}... divided by 2.\n")


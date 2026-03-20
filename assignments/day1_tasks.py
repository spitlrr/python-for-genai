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

print("\nTask 4: Truthy and Falsy Values\n")

def test_truth():
    values = [
        (0, "Falsy", "0 is falsy."),
        (1, "Truthy", "Any non-zero number is truthy."),
        ("", "Falsy", "An empty string is falsy."),
        ("hello", "Truthy", "A non-empty string is truthy."),
        ([], "Falsy", "An empty list is falsy."),
        ([1, 2, 3], "Truthy", "A list with items is truthy."),
        (None, "Falsy", "None type is considered falsy in Python."),
        (True, "Truthy", "Boolean True is truthy."),
        (False, "Falsy", "Boolean False is falsy."),
        ("False", "Truthy", 'This string equals the boolean value "False".')
    ]
    
    print("\n| Value         | Truthiness Status  | Explanation                                 |")
    print("|----------------|---------------------|----------------------------------------------|")
    
    for value, status, explanation in values:
        truthy = "Truthy" if value else "Falsy"
        print(f"| {str(value):<12} | {truthy:^12} | {explanation:<30} |")

test_truth()

print("\nTask 5: Arithmetic Operators\n")

print("This will take two numbers and perform various arithmetic operations on them.\n")

num1 = float(input("Enter the first number: \n"))
num2 = float(input("Enter the second number: \n"))

print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")

print("\nTask 6: Comparison and Logical Operators\n")

age = int(input("Enter your age: \n"))
license = input("Do you have a driver's license? (yes/no) \n").lower() == "yes"
driverEligible = age >= 18 and license
senior = age >= 65
teenager = 13 <= age < 20
voter = age >= 18

print(f"Driver Eligibility: {'Eligible' if driverEligible else 'Not Eligible'}")
print(f"Senior Citizen: {'Yes' if senior else 'No'}")
print(f"Teenager: {'Yes' if teenager else 'No'}")
print(f"Voter: {'Yes' if voter else 'No'}")")
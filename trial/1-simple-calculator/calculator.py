num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice of operation: ")
if choice == "1":
    result = num1 + num2
elif choice == "2":
    result = num1 - num2
elif choice == "3":
    result = num1 * num2
else:
    result = num1/num2
print(result)      
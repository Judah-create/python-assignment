num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divide")

choice = input("Choose: ")

if choice == "1":
    print(num1 + num2)
elif choice == "2":
    print(num1 - num2)
elif choice == "3":
    print(num1 * num2)
elif choice == "4":
    print(num1 / num2)
else:
    print("Wrong choice")

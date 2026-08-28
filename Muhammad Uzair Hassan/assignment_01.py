# 1. Print Name, Father's Name, and Date of Birth using escape sequences
print("--- Task 1: Personal Details ---")
print("Name:\t\tMuhammad Uzair Hassan\nFather's Name:\tSyed Waseem Taqi Shah\nDOB:\t\t21/07/2007\n")


# 2. Small Bio using variables
print("--- Task 2: Small Bio ---")
my_name = "Muhammad Uzair Hassan"
my_course = "Data Analytics with Python"
my_institute = "Saylani Mass IT Training (SMIT)"
print(f"My name is {my_name}. I am learning {my_course} at {my_institute}.\n")


# 3. All Operators in Python
print("--- Task 3: Python Operators ---")
a = 10
b = 3

# Arithmetic Operators
print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponentiation (**):", a ** b)

# Comparison Operators
print("Equal (==):", a == b)
print("Not Equal (!=):", a != b)
print("Greater Than (>):", a > b)
print("Less Than (<):", a < b)
print("Greater Than or Equal (>=):", a >= b)
print("Less Than or Equal (<=):", a <= b)

# Assignment Operators
val = 5
val += 2
val *= 3
print("Assignment result (val):", val)

# Logical Operators
p, q = True, False
print("Logical AND:", p and q)
print("Logical OR:", p or q)
print("Logical NOT:", not p)

# Bitwise Operators
print("Bitwise AND (&):", a & b)
print("Bitwise OR (|):", a | b)
print("Bitwise XOR (^):", a ^ b)
print("Bitwise NOT (~):", ~a)
print("Left Shift (<<):", a << 1)
print("Right Shift (>>):", a >> 1)

# Identity & Membership Operators
nums = [1, 2, 3, 10]
print("Identity (is):", a is a)
print("Identity (is not):", a is not b)
print("Membership (in):", a in nums)
print("Membership (not in):", b not in nums)
print()


# 4. Marks and Percentage Calculation
print("--- Task 4: Marks & Percentage ---")
english = 85
islamiat = 90
maths = 95

total_marks = 300
obtained_marks = english + islamiat + maths
percentage = (obtained_marks / total_marks) * 100

print(f"Total Marks: {total_marks}")
print(f"Obtained Marks: {obtained_marks}")
print(f"Percentage: {percentage:.2f}%\n")


# 5. Swap Two Variables Without a Third Variable
print("--- Task 5: Swapping Variables ---")
x = 15
y = 30
print(f"Before swap: x = {x}, y = {y}")

x, y = y, x

print(f"After swap:  x = {x}, y = {y}\n")


# 6. Circle Area and Circumference
print("--- Task 6: Circle Calculations ---")
pi = 3.14159
radius = 7.0

area = pi * (radius ** 2)
circumference = 2 * pi * radius

print(f"Radius: {radius}")
print(f"Area: {area:.4f}")
print(f"Circumference: {circumference:.4f}\n")


# 7. Discount Amount and Final Price
print("--- Task 7: Discount Calculation ---")
price = 2500.0
discount_percentage = 15.0

discount_amount = (discount_percentage / 100) * price
final_price = price - discount_amount

print(f"Original Price: Rs. {price:.2f}")
print(f"Discount: {discount_percentage}%")
print(f"Discount Amount: Rs. {discount_amount:.2f}")
print(f"Final Price: Rs. {final_price:.2f}")

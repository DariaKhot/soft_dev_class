"""
Daria Khotunitskaya
April 24, Conditional Statement
"""

# Example 1 and 2: if statement
print("\n------ Example 1 and 2: if statement ------")
age = 20
agecode = 123

if age >= 21:
    print("You are an adult!")
    agecode = 200
else:
    print("You are under 21!")
    agecode = 100

print(f"After the 'if' statement, agecode = {agecode}")

# Example 3: statement
print("\n------ Example 3: multi statement ------")
age = 20

if 0 <= age < 21:
    print("You are a minor!")
elif 21 <= age < 65:
    print("You are an adult!")
elif 65 <= age <= 130:
    print("You are a senior citizen!")
else:
    print("Unable to read age!")

print("\n------ Example 4: and operator ------")
temperature = 90
humidity = 60

if 70 <= temperature <= 90 and humidity < 80:
    print("The weather is pleasant")
else:
    print("The weather is not ideal")

print("\n------ Example 5: or operator ------")
day = "Sunday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("You can relax today")
else:
    print("It is a workday")

print("\n------ Example 6: nested conditional statement ------")
number = int(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("The number is zero")
    else:
        print(f"{number} is positive")
else:
    print(f"{number} is negative")

print("\n------ Example 7: username validation ------")
# Username validation: username must have 3+ characters

username = input("Enter a username: ")
username = username.strip()
len_username = len(username)

if len_username >= 3:
    index_whitespace = username.find(" ")
    if index_whitespace == -1:
        print(f"{username} is valid")
    else:
        print("Username CANNOT have whitespace")
else:
    print(f"{username} is INVALID. Username must have 3+ characters")

print("\n------ Example 8: match-case statement ------")
response_code = 404

match response_code:
    case 400:
        print(f"Code = {response_code}. Server CANNOT understand")
    case 401 | 403:
        print(f"Code = {response_code}. Server refused to send back")
    case 404:
        print(f"Code = {response_code}. Server can't find")
    case _:
        print("INVALID CODE")

print ('\n------ Lab Excercise ------")')
# Collect two grades as float values
grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))

# Calculate the average
average = (grade1 + grade2) / 2

# Determine GPA based on the average
if 90 <= average <= 100:
    gpa = "A"
elif 70 <= average <= 89.99:
    gpa = "B"
elif 60 <= average <= 69.99:
    gpa = "C"
elif 0 <= average <= 59.99:
    gpa = "FAIL!"
else:
    gpa = "UNDEFINED!"

# Print the result
print(f"For the average of {average:.2f}, your GPA is {gpa}.")


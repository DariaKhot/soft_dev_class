"""
Daria Khotunitskaya
April 25, loops
"""

print("\n------- Example 1: for loop as a counter -------")
# Print Hello from 0 to 4
for x in range(0, 5):
    print(f"Hello = {x}")

print("\n------- Example 2: for loop in a list -------")
fruits = ['apples', 'oranges', 'grapes', 'kiwis', 'pineapple']

for eachfruitindex in range(0, len(fruits)):
    print(f"Fruit with index {eachfruitindex} = {fruits[eachfruitindex]}")

# Alternative way to loop through a list
print("\n--- Alternative way to loop through a list ---")
for eachfruit in fruits:
    print(eachfruit)


print("\n------- Example 3: for loop with different increment -------")
# For loop to print from 2 to 30, with an increment of 3
for num in range(2, 30, 3):
    print(num)

print("\n------- Example 4: for loop with different decrement -------")
# For loop to print from 10 to 0, with a decrement of 2
for num in range(10, 0, -2):
    print(num)


print("\n------- Example 5: for loop through a string -------")
username = "yes123"
for eachcharacter in username:
    print(eachcharacter)

print("\n------- Example 6: nested conditional statement -------")
# For loop to check how many negative numbers are in the list
numbers = [5, -2, 0, 8, 9, -1]
negativecounter = 0

for eachnumber in numbers:
    if eachnumber < 0:
        negativecounter += 1  # same as negativecounter = negativecounter + 1

# Prompt result
print(f"There is/are {negativecounter} negative number/s")

print("\n------- Example 7: nested conditional statement: operation -------")
# For loop to add all 'odd' numbers
sumodd = 0
for eachnumber in numbers:
    if eachnumber % 2 == 1:
        sumodd += eachnumber

# Prompt result
print(f"The sum of all odd numbers is = {sumodd}")

print("\n------- Example 8: break statement in a loop -------")
# For loop to print from 0 to 10 (exclusive), and terminate the loop when it reaches 5
for n in range(0, 10):
    if n == 5:
        print("Counter reaches 5")
        break
    else:
        print(n)

print("\n------- Example 9: continue statement in a loop -------")
# For loop to add numbers from 0 to 10 (exclusive), except number 5
sumall = 0

for n in range(10):
    if n == 5:
        print("Skipping 5")
        continue
    sumall += n
    print(n)

print(f"Sum = {sumall}")

print("\n------- Example 10: else statement in a for loop -------")
for n in range(6):
    if n == 3:
        break
    print(n)
else:
    print("Loop completed!")

print("\n------- Example 11: while loop as a counter -------")
# While loop to print from 0 to 5 (inclusive) --> 0 1 2 3 4 5
n = 0
while n < 6:
    print(n)
    n += 1

print("\n------- Example 12: while loop as a checkpoint -------")
# While loop to collect and add numbers between -5 and 5
# If the user enters a number not between -5 and 5, the loop terminates

sumusernumber = 0

while True:
    number = int(input("Enter a number between -5 and 5: "))
    if number < -5 or number > 5:
        break
    sumusernumber += number

# Prompt result
print(f"The total sum is = {sumusernumber}")


print("\n------- Example 13: while loop as counting operator -------")
# While loop to count the even numbers (nonzero) in the list

numbers = [2, 0, -5, 1, 8, -6, 7, -3]
index = 0
len_numbers = len(numbers)
evencount = 0

while index < len_numbers:
    if numbers[index] % 2 == 0 and numbers[index] != 0:
        evencount += 1
    index += 1
else:
    print(f"There is/are {evencount} even numbers")



print("\n------- Lab Exercise -------")
# Given list
colors = ['red', 'orange', 'olive', 'magenta', 'green']

# Take color input from user
user_color = input("Enter a color: ").strip().lower()

# Initialize flag
found = False

# For loop to check if color is in the list
for color in colors:
    if user_color == color:
        found = True
        break

# Print result
if found:
    print(f"{user_color} color is in the list")
else:
    print(f"{user_color} color IS NOT in the list")



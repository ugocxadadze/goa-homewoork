i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

i = 1
total_sum = 0
while i <= 10:
    total_sum += i
    i += 1
print("The sum of numbers from 1 to 10 is:", total_sum)

correct_number = 7
guess = 0

while guess != correct_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != correct_number:
        print("Try again!")

print("Congratulations! You guessed the correct number.")

numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
index = 0

while index < len(numbers):
    doubled_numbers.append(numbers[index] * 2)
    index += 1

print("Doubled numbers:", doubled_numbers)

correct_password = "password123"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("Enter the password: ")
    if entered_password != correct_password:
        print("Incorrect password. Please try again.")

print("Password accepted.")

number = 1

# Loop through numbers from 1 to 50
while number <= 50:
    # Check if the number is divisible by 5
    if number % 5 == 0:
        print(number)
    # Increment the number
    number += 1


from datetime import datetime

# Get the current hour
current_hour = datetime.now().hour

# Check if it's morning or afternoon
if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")

number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

temperature = float(input("Enter the temperature in degrees: "))

# Check if it's hot outside
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")




age = int(input("Enter your age: "))

# Check if the age is between 13 and 19 (inclusive)
if 13 <= age <= 19:
    print("You are a teenager!")
else:
    print("You are not a teenager.")




number = 0
while number <= 20:
    print(number)
    number += 2



i = 1
total_sum = 0
while i <= 10:
    total_sum += i
    i += 1
print("The sum of numbers from 1 to 10 is:", total_sum)

correct_number = 7
guess = 0

while guess != correct_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != correct_number:
        print("Try again!")

print("Congratulations! You guessed the correct number.")

numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
index = 0

while index < len(numbers):
    doubled_numbers.append(numbers[index] * 2)
    index += 1

print("Doubled numbers:", doubled_numbers)

correct_password = "password123"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("Enter the password: ")
    if entered_password != correct_password:
        print("Incorrect password. Please try again.")

print("Password accepted.")






for i in range(21):
    print(i)

for i in range(1, 11):
    print(i)

print("Even numbers:")
for i in range(101):
    if i % 2 == 0:
        print(i)

print("\nOdd numbers:")
for i in range(101):
    if i % 2 != 0:
        print(i)




number = int(input("Enter a number: "))
total_sum = 0

for i in range(1, number + 1):
    total_sum += i

print("The sum of all numbers up to", number, "is:", total_sum)





for i in range(1, 51):
    if i % 5 == 0:
        print(i)


#1
def sum_two_numbers(a, b):
    """გამოთვლის ორი რიცხვის ჯამს"""
    return a + b

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

result = sum_two_numbers(num1, num2)
print(f"ორივე რიცხვის ჯამია: {result}")

#2
def add(a, b):
    """მიმატება"""
    return a + b

def subtract(a, b):
    """გამოკლება"""
    return a - b

def multiply(a, b):
    """გამრავლება"""
    return a * b

def divide(a, b):
    """გაყოფა"""
    if b != 0:
        return a / b
    else:
        return "არ შეიძლება გაყოფა ნულით"

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

print(f"სახლურია: {add(num1, num2)}")
print(f"გამოკლებულია: {subtract(num1, num2)}")
print(f"გამრავლებულია: {multiply(num1, num2)}")
print(f"გაყოფილია: {divide(num1, num2)}")

#3
def check_sign(number):
    """გაურკვევლობის შესამოწმებლად რიცხვი დადებითია თუ უარყოფითია"""
    if number > 0:
        return "დადებითი"
    elif number < 0:
        return "უარყოფითი"
    else:
        return "ნული"

num = float(input("შეიყვანეთ რიცხვი: "))


result = check_sign(num)
print(f"რიცხვი {result} არის.")

#4
def check_parity(number):
    """გაურკვევლობის შესამოწმებლად რიცხვი ლუწია თუ კენტი"""
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"


num = int(input("შეიყვანეთ რიცხვი: "))


result = check_parity(num)
print(f"რიცხვი {result} არის.")

#5
def is_multiple_of_five(number):
    """გაურკვევლობის შესამოწმებლად რიცხვი ხუთის ჯერადია თუ არა"""
    if number % 5 == 0:
        return True
    else:
        return False

num = int(input("შეიყვანეთ რიცხვი: "))

if is_multiple_of_five(num):
    print(f"რიცხვი {num} ხუთის ჯერადია.")
else:
    print(f"რიცხვი {num} არ არის ხუთის ჯერადი.")
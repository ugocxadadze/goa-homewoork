#1
def max_of_two(a, b):
    return a if a > b else b


print(max_of_two(5, 8))  

#2
def check_even_odd(number):
    if number % 2 == 0:
        return "ლუწი"  
    else:
        return "კენტი"  

# გამოსახულება:
print(check_even_odd(4))  
print(check_even_odd(7))  

#3
def greet_user(name):
    print(f"Hello {name}!")


greet_user("Davit")  

#4
import random

def guess_number():
    secret_number = random.randint(1, 100)  
    while True:
        try:
            guess = int(input("გთხოვთ გამოიცნოთ რიცხვი (1-100): "))
            if guess == secret_number:
                print("სწორია ყოჩაღ!")
                break
            else:
                print("არასწორია, თავიდან სცადე.")
        except ValueError:
            print("გთხოვთ შეიყვანოთ ვალიდური რიცხვი.")


guess_number()
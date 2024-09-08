def calculator():
    """
    ეკითხება მომხმარებელს ორ რიცხვს და მათემატიკურ ოპერაციას,
    შემდეგ ასრულებს მოთხოვნილ ოპერაციას და დაბეჭდავს შედეგს.
    """
    try:
        # მიიღოს ორი რიცხვი მომხმარებლიდან
        num1 = float(input("გთხოვთ, ჩაწერეთ პირველი რიცხვი: "))
        num2 = float(input("გთხოვთ, ჩაწერეთ მეორე რიცხვი: "))

        # მიაწვდოს ოპერაციების ტიპები
        print("აირჩიეთ მათემატიკური ოპერაცია:")
        print("1. დამატება (+)")
        print("2. გამოკლება (-)")
        print("3. გამრავლება (*)")
        print("4. გაყოფა (/)")
        
        operation = input("გთხოვთ, ჩაწერეთ ოპერაციის სიმბოლო (+, -, *, /): ").strip()

        # შესრულება შესაბამისი ოპერაციის მიხედვით
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("ციფრის გაყოფა 0-ით არ შეიძლება.")
                return
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("არასწორი ოპერაციის სიმბოლო. გთხოვთ, აირჩიოთ სწორი ოპერაცია.")
    
    except ValueError:
        print("გთხოვთ, ჩაწეროთ მხოლოდ რიცხვები.")

# ფუნქციის გამოძახება
calculator()
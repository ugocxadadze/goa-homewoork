def add_two_numbers():
    """
    ეკითხება მომხმარებელს ორ რიცხვს და აჯამებს მათ.
    """
    try:
        
        num1 = float(input("გთხოვთ, ჩაწერეთ პირველი რიცხვი: "))
        num2 = float(input("გთხოვთ, ჩაწერეთ მეორე რიცხვი: "))

        
        total = num1 + num2
        print(f"ორივე რიცხვის ჯამია: {total}")

    except ValueError:
        print("გთხოვთ, ჩაწეროთ მხოლოდ რიცხვები.")

add_two_numbers()
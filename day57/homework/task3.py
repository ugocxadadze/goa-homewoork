def check_odd_even():
    """
    
    """
    try:
        # მიიღოს რიცხვი მომხმარებლიდან
        number = int(input("გთხოვთ, ჩაწერეთ რიცხვი: "))
        
        # განსაზღვროს რიცხვის ტიპი
        if number % 2 == 0:
            print(f"რიცხვი {number} არის ლუწი.")
        else:
            print(f"რიცხვი {number} არის კენტი.")
    
    except ValueError:
        print("გთხოვთ, ჩაწეროთ მხოლოდ რიცხვი.")

# ფუნქციის გამოძახება
check_odd_even()
def time_travel():
    """
    ეკითხება მომხმარებელს მის ასაკს, მიმდინარე წელს, დროში მოგზაურობის ხანგრძლივობას და მომავალი თუ წარსული მოგზაურობის სურვილს,
    და გამოყოფს შემდეგ წელიწადს და ასაკს.
    """
    try:
        # მიიღოს ასაკი, მიმდინარე წელი და დროში მოგზაურობის ხანგრძლივობა
        current_age = int(input("გთხოვთ, ჩაწერეთ თქვენი ახლანდელი ასაკი: "))
        current_year = int(input("გთხოვთ, ჩაწერეთ მიმდინარე წელი: "))
        travel_years = int(input("გთხოვთ, ჩაწერეთ რამდენი ხანით სურს დროში მოგზაურობა: "))
        
        # არჩევანი მომავალი ან წარსული მოგზაურობის
        direction = input("გთხოვთ, ჩაწერეთ 'მომავალი' თუ 'წარსული': ").strip().lower()

        if direction == 'მომავალი':
            future_year = current_year + travel_years
            future_age = current_age + travel_years
            print(f"თქვენი მოგზაურობის შემდეგ წელი იქნება {future_year}, და თქვენი ასაკი იქნება {future_age}.")
        elif direction == 'წარსული':
            past_year = current_year - travel_years
            past_age = current_age - travel_years
            if past_age < 0:
                print("წარსულში მოგზაურობა თქვენი ასაკის გამო შეუძლებელია.")
            else:
                print(f"თქვენი მოგზაურობის შემდეგ წელი იქნება {past_year}, და თქვენი ასაკი იქნება {past_age}.")
        else:
            print("არასწორი არჩევანი, გთხოვთ, ჩაწერეთ 'მომავალი' ან 'წარსული'.")
    
    except ValueError:
        print("გთხოვთ, ჩაწეროთ მხოლოდ რიცხვები.")

# ფუნქციის გამოძახება
time_travel()
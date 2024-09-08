accounts = {}

def create_account():
    """ახალი ანგარიშის შექმნა"""
    username = input("შეიყვანეთ თქვენი მომხმარებლის სახელი: ")
    if username in accounts:
        print("ამ სახელით უკვე არსებობს ანგარიში.")
    else:
        password = input("შეიყვანეთ პაროლი: ")
        accounts[username] = {'password': password, 'balance': 0}
        print("ანგარიში წარმატებით შექმნილია!")

def login():
    """მომხმარებლის შესვლა"""
    username = input("შეიყვანეთ თქვენი მომხმარებლის სახელი: ")
    password = input("შეიყვანეთ პაროლი: ")
    if username in accounts and accounts[username]['password'] == password:
        return username
    else:
        print("მომხმარებლის სახელი ან პაროლი არასწორია.")
        return None

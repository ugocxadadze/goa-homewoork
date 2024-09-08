#1

def add_one():
    try:
       
        number = float(input("გთხოვთ შეიყვანოთ რიცხვი: "))
       
        result = number + 1
       
        print(f"შედეგი: {result}")
    except ValueError:
        print("გთხოვთ, შეიყვანოთ სწორად რიცხვი.")


add_one()


#2
def check_number():
    try:
       
        number = float(input("გთხოვთ შეიყვანოთ რიცხვი: "))
        
        
        if number > 10:
            return "მაგარია!"
        else:
            return "რიცხვი 10-ზე ნაკლებია."

    except ValueError:
        return "გთხოვთ, შეიყვანოთ სწორად რიცხვი."


result = check_number()
print(result)


#3
def find_minimum():
    try:
       
        num1 = float(input("გთხოვთ შეიყვანოთ პირველი რიცხვი: "))
        num2 = float(input("გთხოვთ შეიყვანოთ მეორე რიცხვი: "))
        
       
        minimum = min(num1, num2)
        return minimum

    except ValueError:
        return "გთხოვთ, შეიყვანოთ სწორად რიცხვები."

result = find_minimum()
print(f"უმცირესი რიცხვია: {result}")


#4
def get_text_length():
   
    text = input("გთხოვთ შეიყვანოთ ტექსტი: ")
    
   
    length = len(text)
    
   
    return length


text_length = get_text_length()
print(f"ტექსტის სიგრძეა: {text_length}")


#5
def add_two_numbers():
    try:
       
        num1 = float(input("გთხოვთ შეიყვანოთ პირველი რიცხვი: "))
        num2 = float(input("გთხოვთ შეიყვანოთ მეორე რიცხვი: "))
        
       
        total = num1 + num2
        
       
        return total
    
    except ValueError:
        return "გთხოვთ, შეიყვანოთ სწორად რიცხვები."


result = add_two_numbers()
print(f"რიცხვების ჯამია: {result}")


#6
def check_number_sign():
    try:
       
        number = float(input("გთხოვთ შეიყვანოთ რიცხვი: "))
        
       
        if number > 0:
            return "დადებითი"
        elif number < 0:
            return "უარყოფითი"
        else:
            return "ნულოვანი"  

    except ValueError:
        return "გთხოვთ, შეიყვანოთ სწორად რიცხვი."


result = check_number_sign()
print(result)



#7
def is_even():
    try:
        
        number = float(input("გთხოვთ შეიყვანოთ რიცხვი: "))
        
        
        if number % 2 == 0:
            return True
        else:
            return False
    
    except ValueError:
        return "გთხოვთ, შეიყვანოთ სწორად რიცხვი."

result = is_even()
print(result)


#8
def add_and_add_five():
    try:
        
        num1 = float(input("გთხოვთ შეიყვანოთ პირველი რიცხვი: "))
        num2 = float(input("გთხოვთ შეიყვანოთ მეორე რიცხვი: "))
        
        total = num1 + num2
        
        result = total + 5
        
        return result
    
    except ValueError:
        return "გთხოვთ, შეიყვანოთ სწორად რიცხვები."


result = add_and_add_five()
print(f"ჯამი 5-ს დამატებით: {result}")
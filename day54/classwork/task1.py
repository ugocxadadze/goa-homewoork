basket = ["ვაშლი", "ნატროკა", "ბანანი", "სტროფი", "ქლიავი", "კივი", "ყურძენი"]

favorite_fruit = input("რომელი ხილი არის თქვენი საყვარელი? ")

if favorite_fruit in basket:
    print("Good choice!")
else:
    print("Fruit not in basket.")


#2

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))


if num1 > num2:
    smaller = num2
    larger = num1
else:
    smaller = num1
    larger = num2


print("უმცირესიდან უდიდესამდე რიცხვები:")
for number in range(smaller, larger + 1):

    if number % 2 == 0:
        parity = "ლუწია"
    else:
        parity = "კენტია"
    
  
    print(f"{number} - {parity}")